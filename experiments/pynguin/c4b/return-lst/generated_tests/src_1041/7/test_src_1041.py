# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1041 as module_0


def test_case_0():
    str_0 = "y~WS4T3z@51Pf1"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_1():
    str_0 = "z!2_js1#%iM}c<_,/yI]"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "!KVr|@sG/"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


def test_case_4():
    str_0 = '("N/RGGi{WyX#<rc+//C'
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_5():
    str_0 = '("N/RGGi{Wy\t#<rc///C'
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*str_0)
    list_1 = module_0.func(*list_0)
    var_1 = module_0.func(*list_1)