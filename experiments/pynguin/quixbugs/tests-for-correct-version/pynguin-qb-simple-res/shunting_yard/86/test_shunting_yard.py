# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shunting_yard as module_0


def test_case_0():
    str_0 = "0"
    var_0 = module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.shunting_yard(list_0)
    var_1 = module_0.shunting_yard(list_0)
    var_2 = module_0.shunting_yard(var_0)
    var_3 = module_0.shunting_yard(var_1)
    module_0.shunting_yard(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "V\\fPS2fb"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "/+z}3OP\x0b%8dVkft^"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "/+/zD3OP\x0b%8dVkft^"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "+//z}3OP\x0b%8d`kft^"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    int_0 = 859
    list_0 = [int_0]
    bool_0 = False
    tuple_0 = (int_0, list_0, bool_0)
    var_0 = module_0.shunting_yard(list_0)
    var_1 = module_0.shunting_yard(tuple_0)
    str_0 = "+//+z}3OP\x0b%8dkft^"
    module_0.shunting_yard(str_0)