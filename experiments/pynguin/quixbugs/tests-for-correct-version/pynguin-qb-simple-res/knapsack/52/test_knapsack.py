# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "fB>m$mr;a^Ghz>-"
    module_0.knapsack(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    str_0 = "fB>m$mr;a^Ghz>-"
    var_0 = module_0.knapsack(str_0, dict_0)
    assert var_0 == 0
    module_0.knapsack(var_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 1367
    module_0.knapsack(int_0, int_0)


def test_case_3():
    bool_0 = True
    bytes_0 = b"\x12\xbc"
    tuple_0 = (bytes_0,)
    var_0 = module_0.knapsack(bool_0, tuple_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    bytes_0 = b"\x0c\x9c"
    tuple_0 = (bytes_0,)
    var_0 = module_0.knapsack(bool_0, tuple_0)
    assert var_0 == 0
    object_0 = module_1.object()
    int_0 = 3265
    var_1 = module_0.knapsack(int_0, tuple_0)
    assert var_1 == 156
    module_0.knapsack(var_1, int_0)