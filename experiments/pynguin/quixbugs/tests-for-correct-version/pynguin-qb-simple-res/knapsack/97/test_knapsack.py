# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"k\xfb\xc77\x0f\x94\xee\xed\x7f\xd4G\xe9\xc3\x7f\xaa\xa5\xca\xcc"
    module_0.knapsack(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    var_0 = module_0.knapsack(tuple_0, tuple_0)
    assert var_0 == 0
    str_0 = "DQL<\x0c=-X]%KA=uv"
    module_0.knapsack(var_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.knapsack(bool_0, bool_0)


def test_case_3():
    tuple_0 = ()
    str_0 = "w|n@L 'jeZe:8l7-lD"
    var_0 = module_0.knapsack(str_0, tuple_0)
    assert var_0 == 0
    set_0 = {str_0, str_0, var_0, var_0}
    tuple_1 = (set_0,)
    var_1 = module_0.knapsack(var_0, tuple_1)
    assert var_1 == 0


@pytest.mark.xfail(strict=True)
def test_case_4():
    tuple_0 = ()
    var_0 = module_0.knapsack(tuple_0, tuple_0)
    assert var_0 == 0
    set_0 = {tuple_0, tuple_0, var_0}
    tuple_1 = (set_0,)
    int_0 = 1409
    module_0.knapsack(int_0, tuple_1)