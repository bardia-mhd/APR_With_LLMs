# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"T\xfa\x88\xc5\xa5<\xa9\xdd9\x8a\xb1\xae\xcf"
    module_0.knapsack(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    bool_0 = False
    var_0 = module_0.knapsack(bool_0, list_0)
    assert var_0 == 0
    list_1 = [list_0]
    module_0.knapsack(bool_0, list_1)


def test_case_2():
    int_0 = -165
    list_0 = [int_0, int_0]
    bool_0 = False
    list_1 = [list_0]
    var_0 = module_0.knapsack(bool_0, list_1)
    assert var_0 == 0


def test_case_3():
    int_0 = -3634
    list_0 = [int_0, int_0]
    bool_0 = True
    list_1 = [list_0]
    var_0 = module_0.knapsack(bool_0, list_1)
    assert var_0 == 0


def test_case_4():
    int_0 = 1095
    list_0 = [int_0, int_0]
    bool_0 = True
    list_1 = [list_0]
    var_0 = module_0.knapsack(bool_0, list_1)
    assert var_0 == 0
    object_0 = module_1.object()