# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shunting_yard as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "RaE"
    module_0.shunting_yard(str_0)


def test_case_1():
    str_0 = "E"
    var_0 = module_0.shunting_yard(str_0)


def test_case_2():
    bytes_0 = b""
    var_0 = module_0.shunting_yard(bytes_0)
    var_1 = module_0.shunting_yard(bytes_0)
    var_2 = module_0.shunting_yard(var_0)
    var_3 = module_0.shunting_yard(var_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    module_0.shunting_yard(none_type_0)


def test_case_4():
    bool_0 = False
    tuple_0 = (bool_0,)
    set_0 = {tuple_0, bool_0, bool_0, tuple_0}
    var_0 = module_0.shunting_yard(set_0)
    tuple_1 = ()
    var_1 = module_0.shunting_yard(tuple_1)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "++*ci2`1Q^\n%Mx:c\raR9"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "++**i2`1Q^\n%Mx^c\raR9"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    list_0 = []
    var_0 = module_0.shunting_yard(list_0)
    var_1 = module_0.shunting_yard(var_0)
    var_2 = module_0.shunting_yard(var_0)
    var_3 = module_0.shunting_yard(var_0)
    var_4 = module_0.shunting_yard(var_2)
    str_0 = "++**+2`1Q^\n%Mx^c\raR9"
    module_0.shunting_yard(str_0)