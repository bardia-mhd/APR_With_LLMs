# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b'.Vyi7\x03T\xba;\xa6\x85n\x12\xfd!\xdb\x83\xce\xa7"'
    module_0.knapsack(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ""
    var_0 = module_0.knapsack(str_0, str_0)
    assert var_0 == 0
    str_1 = "/(Gs'!nX"
    module_0.knapsack(str_1, str_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -211.9342
    module_0.knapsack(float_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    tuple_0 = ()
    var_0 = module_0.knapsack(tuple_0, tuple_0)
    assert var_0 == 0
    dict_0 = {var_0: var_0, var_0: tuple_0, tuple_0: var_0}
    tuple_1 = (dict_0, var_0)
    module_0.knapsack(var_0, tuple_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    bytes_0 = b"\xa2\xebY\x02\x18\xed\x1c\n?\x00"
    list_1 = [list_0, bytes_0, bool_0]
    module_0.knapsack(bool_0, list_1)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    bytes_0 = b"\xd5u"
    list_1 = [list_0, bytes_0, bool_0]
    module_0.knapsack(bool_0, list_1)