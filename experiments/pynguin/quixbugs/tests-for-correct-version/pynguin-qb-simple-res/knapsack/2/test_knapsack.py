# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = '"_G_V|Ki2-5&F?KH\rjt'
    module_0.knapsack(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    var_0 = module_0.knapsack(tuple_0, tuple_0)
    assert var_0 == 0
    str_0 = '"_G_V|Ki2-5&F?KH\rjt'
    module_0.knapsack(str_0, str_0)


def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    list_1 = [list_0]
    var_0 = module_0.knapsack(bool_0, list_1)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    bytes_0 = b"G\x94"
    list_0 = [bytes_0, bool_0, bytes_0]
    module_0.knapsack(bool_0, list_0)