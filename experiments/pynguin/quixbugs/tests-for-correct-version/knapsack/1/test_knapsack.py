# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    tuple_0 = ()
    var_0 = module_0.knapsack(tuple_0, tuple_0)
    assert var_0 == 0
    bytes_0 = b":\x12N\xc5\x1c\xfa+\xa9\xd8 \xb2@"
    module_0.knapsack(var_0, bytes_0)


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.knapsack(tuple_0, tuple_0)
    assert var_0 == 0


def test_case_2():
    bytes_0 = b"Y\x88"
    tuple_0 = (bytes_0, bytes_0, bytes_0)
    bool_0 = True
    var_0 = module_0.knapsack(bool_0, tuple_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_3():
    tuple_0 = ()
    var_0 = module_0.knapsack(tuple_0, tuple_0)
    assert var_0 == 0
    bytes_0 = b"\x00\xb3"
    tuple_1 = (bytes_0, bytes_0, bytes_0)
    bool_0 = True
    var_1 = module_0.knapsack(bool_0, tuple_1)
    assert var_1 == 537
    module_0.knapsack(tuple_1, bool_0)