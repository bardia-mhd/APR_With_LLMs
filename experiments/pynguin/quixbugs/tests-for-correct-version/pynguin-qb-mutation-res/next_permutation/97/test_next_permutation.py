# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import next_permutation as module_0


def test_case_0():
    str_0 = "8k_xS3rO "
    var_0 = module_0.next_permutation(str_0)


def test_case_1():
    list_0 = []
    var_0 = module_0.next_permutation(list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    complex_0 = -1253.49 - 1236j
    module_0.next_permutation(complex_0)