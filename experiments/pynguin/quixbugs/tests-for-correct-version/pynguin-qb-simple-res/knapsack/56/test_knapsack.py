# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "4nT-*(bc$"
    module_0.knapsack(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    module_0.knapsack(set_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.knapsack(none_type_0, none_type_0)


def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    tuple_0 = (list_0, list_0, list_0, list_0)
    var_0 = module_0.knapsack(bool_0, tuple_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    bytes_0 = b"\r\xa1"
    float_0 = -1422.243
    tuple_0 = (bytes_0, bytes_0, float_0, bool_0)
    module_0.knapsack(bool_0, tuple_0)