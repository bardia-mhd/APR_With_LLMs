# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shunting_yard as module_0


def test_case_0():
    bytes_0 = b"U\x10l"
    var_0 = module_0.shunting_yard(bytes_0)


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.shunting_yard(tuple_0)


def test_case_2():
    str_0 = "="
    var_0 = module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ";q"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "-*h!@q\x0ceccek]h:H<%"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "**h!@q\x0ceccek]h:H<%"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "-**h!q\x0cccVk]h:<%C"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    float_0 = 2396.277298
    set_0 = {float_0, float_0}
    var_0 = module_0.shunting_yard(set_0)
    var_1 = module_0.shunting_yard(set_0)
    var_2 = module_0.shunting_yard(set_0)
    tuple_0 = ()
    str_0 = "-*-h!@q\x0ce&ccVk]h:H(%"
    var_3 = module_0.shunting_yard(set_0)
    var_4 = module_0.shunting_yard(tuple_0)
    module_0.shunting_yard(str_0)