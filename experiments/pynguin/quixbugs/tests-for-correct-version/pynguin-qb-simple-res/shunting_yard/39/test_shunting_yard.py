# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shunting_yard as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "98mUALSKpsOq~D\t;'5."
    module_0.shunting_yard(str_0)


def test_case_1():
    str_0 = "8"
    var_0 = module_0.shunting_yard(str_0)


def test_case_2():
    int_0 = 347
    dict_0 = {int_0: int_0}
    set_0 = module_0.shunting_yard(dict_0)
    var_0 = module_0.shunting_yard(set_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = '-+?%W,TkE"l'
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = '-+/?%W,TkE"l'
    module_0.shunting_yard(str_0)