# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xad\x01\x08\xc4\xc9.\xfb\xe4\x8a\x95\x1c\xc7\\\x84"
    module_0.knapsack(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ""
    var_0 = module_0.knapsack(str_0, str_0)
    assert var_0 == 0
    bytes_0 = b"[\xae`\x9a"
    module_0.knapsack(var_0, bytes_0)


def test_case_2():
    bytes_0 = b"6\x00"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    bool_0 = True
    var_0 = module_0.knapsack(bool_0, list_0)
    assert var_0 == 0


def test_case_3():
    bytes_0 = b"6\x00"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    bool_0 = True
    var_0 = module_0.knapsack(bool_0, list_0)
    assert var_0 == 0
    int_0 = 1226
    var_1 = module_0.knapsack(int_0, list_0)