# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "AeFv^2-.<2"
    module_0.knapsack(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    bytes_0 = b"\x12\xc2\x9e\xf5\x15\xb3\xa9\x07"
    var_0 = module_0.knapsack(bytes_0, list_0)
    assert var_0 == 0
    module_0.knapsack(var_0, bytes_0)


def test_case_2():
    bytes_0 = b"\x83%"
    tuple_0 = (bytes_0, bytes_0)
    bool_0 = True
    var_0 = module_0.knapsack(bool_0, tuple_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_3():
    list_0 = []
    bytes_0 = b"\x02\x16@~M\xc5\xade\x844\xdc\x9f9\xd1%A9\x8a"
    var_0 = module_0.knapsack(bytes_0, list_0)
    assert var_0 == 0
    tuple_0 = (var_0, var_0)
    dict_0 = {var_0: tuple_0, var_0: tuple_0, bytes_0: var_0}
    bool_0 = True
    module_0.knapsack(bool_0, dict_0)