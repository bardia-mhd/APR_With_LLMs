# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "<ad0"
    module_0.knapsack(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    object_0 = module_1.object(**dict_0)
    var_0 = module_0.knapsack(object_0, dict_0)
    assert var_0 == 0
    str_0 = "L~Z"
    module_0.knapsack(object_0, str_0)


def test_case_2():
    dict_0 = {}
    list_0 = [dict_0, dict_0]
    int_0 = -4219
    list_1 = [list_0]
    var_0 = module_0.knapsack(int_0, list_1)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_3():
    dict_0 = {}
    list_0 = [dict_0, dict_0]
    int_0 = 2161
    list_1 = [list_0]
    module_0.knapsack(int_0, list_1)