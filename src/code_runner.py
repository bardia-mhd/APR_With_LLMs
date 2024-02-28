from test_generator import TestGenerator
import pandas as pd
import subprocess
import ast


import time
from functools import wraps


def retry_decorator(max_retries=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retry_count = 0
            while retry_count < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Exception occurred: {e}")
                    retry_count += 1
                    print(f"Retrying... (Attempt {retry_count} of {max_retries})")
                    time.sleep(delay)
            print(f"Max retries reached. Giving up.")

        return wrapper

    return decorator


class CodeRunner:
    def __init__(self, is_func, is_qb, is_iterative, meta_data_config) -> None:
        self.is_func = is_func
        self.is_qb = is_qb
        self.is_iteravtive = is_iterative
        # self.meta_data_config = meta_data_config
        self.test_generator = TestGenerator(config=meta_data_config)

        if is_func:
            self.df_submissions = pd.read_csv(
                "data2/2acc_copy/cb_submission_res_2acc_alt.csv"
            )
            self.df_testcases = pd.read_csv("data2/2acc_copy/cb_testcase_res_2acc.csv")

    def prepare_data(self, problem_id, author_id) -> tuple:
        df = self.df_submissions[
            (self.df_submissions["problems_id"] == problem_id)
            & (self.df_submissions["author"] == author_id)
        ]["func_sourceCode_yield"]
        df_acc_other = self.df_submissions[
            (self.df_submissions["verdicts_id"] == 1)
            & (self.df_submissions["problems_id"] == problem_id)
            & (self.df_submissions["author"] != author_id)
        ]["func_sourceCode_yield"]
        acc1 = df.values.tolist()[0]
        rej = df.values.tolist()[1]
        acc2 = df_acc_other.values.tolist()[0]

        df_testcase = self.df_testcases[self.df_testcases["problems_id"] == problem_id]
        test_cases = df_testcase[["inputdata"]].to_dict("records")

        return acc1, acc2, rej, test_cases[0]

    def create_unnitest(self, buggy_code, acc_code, test_cases):
        with open(f"temp_acc_qb.py", "w") as f:
            f.write(acc_code)
        with open(f"temp_bug_qb.py", "w") as f:
            f.write(buggy_code)

        unittest_str = f"""
import unittest
from temp_bug_qb import func as buggy_source
from temp_acc_qb import func as accepted_source

class TestFunctions(unittest.TestCase):
                
"""

        for i, test_case in enumerate(test_cases):
            input_data = test_case["inputdata"]
            if "\n" in input_data:
                input_data = list(input_data.split("\n"))

            unittest_str = (
                unittest_str
                + f"""

    def test{i}(self):
        input_{i} = "{input_data}"
        self.assertEqual(list(buggy_source(input_{i})), list(accepted_source(input_{i})))
            
"""
            )

        unittest_str += """

if __name__ == '__main__':
    unittest.main()  
    
    """

        with open(f"temp_test_case.py", "w") as f:
            f.write(unittest_str)

    def generate_bet_test(self, problem_id, author_id) -> list:
        acc1, _, rej, test_case = self.prepare_data(problem_id, author_id)
        test_cases = self.test_generator.generate_test(rej, acc1, test_case, None)
        return test_cases

    def change_test_to_dict(test_case) -> list:
        data_list = []
        for fault_test in test_case:
            if fault_test:
                try:
                    data_list.append(ast.literal_eval(fault_test.replace("python", "")))
                except Exception as e:
                    print(e)
                    continue
        return data_list

    def check_test(self, problem_id, author_id):

        acc1, _, rej, test_case = self.prepare_data(problem_id, author_id)
        test_case = self.test_generator.generate_test(rej, acc1, test_case, None)

        data_list = self.change_test_to_dict(test_case)

        self.create_unnitest(rej, acc1, data_list)
        try:
            process = subprocess.run(
                ["python", f"temp_test_case.py"], capture_output=True, timeout=5
            )
        except subprocess.TimeoutExpired:
            process = "Timeout"
        output = str(process)
        if ("AssertionError" not in output) and ("temp_bug_qb.py" not in output):
            for i in range(10):
                self.create_unnitest(rej, acc1, data_list)
                try:
                    process = subprocess.run(
                        ["python", f"temp_test_case.py"], capture_output=True, timeout=1
                    )
                except subprocess.TimeoutExpired:
                    process = "Timeout"
                output = str(process)
                if ("AssertionError" in output) or ("temp_bug_qb.py" in output):
                    return "Found1"
            return str(process)
        else:
            return "Found1"

    @retry_decorator(max_retries=3, delay=1)
    def run(self):
        if self.is_func:
            grouped = (
                self.df_submissions.groupby(["author", "problems_id"])["diff_ratio"]
                .mean()
                .reset_index()
            )
            grouped = grouped.sort_values("diff_ratio", ascending=False)
            top_10_percent = int(len(grouped) * 0.1)
            result = grouped.iloc[2 * top_10_percent : 3 * top_10_percent][
                ["author", "problems_id"]
            ].values.tolist()

            for i in result:
                self.check_test(i[1], i[0])
        else:
            self.check_test(1, 1)
        return "Done"
