# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x1b\x88\xb3\x83\xecSz\x9aq\xc27\xd9\xfe8\xcdMc"
    module_0.knapsack(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    var_0 = module_0.knapsack(tuple_0, tuple_0)
    assert var_0 == 0
    set_0 = {var_0, var_0}
    module_0.knapsack(set_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    tuple_0 = ()
    var_0 = module_0.knapsack(tuple_0, tuple_0)
    assert var_0 == 0
    set_0 = {tuple_0, var_0, var_0}
    list_0 = [set_0, var_0, var_0]
    module_0.knapsack(var_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    tuple_0 = ()
    bool_0 = True
    dict_0 = {bool_0: tuple_0, tuple_0: tuple_0}
    tuple_1 = (dict_0,)
    module_0.knapsack(bool_0, tuple_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 2802
    list_0 = [int_0, int_0]
    tuple_0 = (list_0, list_0)
    var_0 = module_0.knapsack(int_0, tuple_0)
    assert var_0 == 2802
    bool_0 = True
    module_0.knapsack(bool_0, bool_0)