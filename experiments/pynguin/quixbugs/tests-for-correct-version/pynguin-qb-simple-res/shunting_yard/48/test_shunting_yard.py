# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shunting_yard as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = " cHbC28hUg[x|<W#6"
    module_0.shunting_yard(str_0)


def test_case_1():
    str_0 = "-"
    var_0 = module_0.shunting_yard(str_0)


def test_case_2():
    tuple_0 = ()
    var_0 = module_0.shunting_yard(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    module_0.shunting_yard(none_type_0)


def test_case_4():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.shunting_yard(list_0)
    var_1 = module_0.shunting_yard(var_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = '+*."_UEC%#5wl\x0czq '
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = '+*-"_EC%#5wl\x0czq '
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    bytes_0 = b"\xd1n"
    set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
    var_0 = module_0.shunting_yard(bytes_0)
    str_0 = '+/*-"_EC%#5w\x0czq '
    var_1 = module_0.shunting_yard(set_0)
    var_2 = module_0.shunting_yard(var_1)
    module_0.shunting_yard(str_0)


def test_case_8():
    str_0 = "+*"
    var_0 = module_0.shunting_yard(str_0)