# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1573 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    str_0 = "E_RNi;T LvViIZ>{Sr"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_2():
    str_0 = "K9\x0ccP~;wVV7JC"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, var_0, str_0, str_0, str_0, str_0]
    var_1 = module_0.func(*list_0)


def test_case_3():
    str_0 = "9\x0ccP~;wVV7JC"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_4():
    str_0 = "KK"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


def test_case_5():
    str_0 = "VK"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "VKK"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, str_0]
    var_1 = module_0.func(*list_0)
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "KVVKVV"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()