# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1937 as module_0


def test_case_0():
    str_0 = 'dq>*,D"|dWRID'
    var_0 = module_0.func(*str_0)
    assert var_0 == "D"


def test_case_1():
    str_0 = '@gEWiu\nk"w({9k82'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == '@gEWiu\nk"w({9k82'


def test_case_2():
    str_0 = '\x0cq*,D"jW#I'
    var_0 = module_0.func(*str_0)
    assert var_0 == "\x0c"


def test_case_3():
    str_0 = "lIZ"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Liz"


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = '"IZ'
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == '"IZ'
    str_1 = 'dq>*,c"|SWRID'
    var_1 = module_0.func(*str_1)
    assert var_1 == "D"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "IZ"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "iz"
#    module_0.func()