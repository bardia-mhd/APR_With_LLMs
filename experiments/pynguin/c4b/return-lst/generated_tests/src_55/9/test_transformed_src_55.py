# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_55 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "8\r{*\x0b"
    var_0 = module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = "1"
    var_0 = module_0.func(*str_0)


def test_case_3():
    list_0 = []
    list_1 = [list_0]
    var_0 = module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "a8"
    var_0 = module_0.func(*str_0)
    list_0 = [var_0, str_0, str_0, var_0]
    var_1 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "h"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "h1"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "W1hO"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_1.object()
#    module_1.object(*list_0, **str_0)


#@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "a8"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = "h8"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    str_1 = "88\ri{*>"
    var_1 = module_0.func(*list_0)
    list_1 = [str_1, str_1, str_0, str_1]
    var_2 = module_0.func(*list_1)
    object_0 = module_1.object()
    var_3 = module_0.func(*str_1)
#    module_1.object(**var_1)


#@pytest.mark.xfail(strict=True)
def test_case_10():
    str_0 = ""
    str_1 = "a1"
    list_0 = [str_1, str_0, str_0, str_1]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_1)
#    module_1.object(**list_0)


#@pytest.mark.xfail(strict=True)
def test_case_11():
    str_0 = "C8-1{w+heGX+lQ1x(mj`"
    int_0 = 3319
    dict_0 = {str_0: str_0, str_0: int_0}
    list_0 = [str_0, str_0, dict_0, int_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_12():
    str_0 = "aa8"
    var_0 = module_0.func(*str_0)
    str_1 = "88\ri{*>"
    list_0 = [str_0, str_0, str_1, var_0]
    var_1 = module_0.func(*list_0)
    var_2 = module_0.func(*str_1)
#    module_0.func()