# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "k,f+|d*V}A)S@"
    module_0.knapsack(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    var_0 = module_0.knapsack(tuple_0, tuple_0)
    assert var_0 == 0
    str_0 = "k,f+|d*V}A)S@"
    module_0.knapsack(var_0, str_0)


def test_case_2():
    str_0 = "d$"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    bool_0 = False
    var_0 = module_0.knapsack(bool_0, list_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "d$"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    bool_0 = True
    module_0.knapsack(bool_0, list_0)


def test_case_4():
    bool_0 = True
    tuple_0 = (bool_0, bool_0)
    list_0 = [tuple_0]
    var_0 = module_0.knapsack(bool_0, list_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 2501
    int_1 = 631
    set_0 = {int_0, int_0, int_0, int_1}
    list_0 = []
    tuple_0 = (set_0, list_0)
    module_0.knapsack(int_0, tuple_0)