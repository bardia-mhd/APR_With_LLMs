# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2668 as module_0


def test_case_0():
    str_0 = "1Hp(3tZn2h"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "10p(6t%Z\\/Czp>\r"
    var_0 = module_0.func(*str_0)


def test_case_3():
    str_0 = "1o(GtL~ZU2h"
    bool_0 = True
    list_0 = [bool_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "10p(6t%Z\\/Czp>\r"
    float_0 = 3935.0
    list_0 = [float_0, str_0, float_0]
    module_0.func(*list_0)