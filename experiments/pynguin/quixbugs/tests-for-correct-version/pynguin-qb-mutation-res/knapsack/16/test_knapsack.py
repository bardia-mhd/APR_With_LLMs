# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"12"
    module_0.knapsack(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    module_0.knapsack(set_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 3254
    list_0 = [int_0, int_0]
    list_1 = [list_0]
    var_0 = module_0.knapsack(int_0, list_1)
    assert var_0 == 3254
    module_0.knapsack(list_0, list_0)