# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2223 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    dict_0 = {}
    list_0 = [dict_0, dict_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    dict_0 = {}
    list_0 = [dict_0, dict_0]
    var_0 = module_0.func(*list_0)
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    dict_0 = {}
    str_0 = "A4q`>A:7 Rfd\nDn ,\x0bm|"
    var_0 = module_0.func(*str_0)
    list_0 = [dict_0, dict_0]
    var_1 = module_0.func(*list_0)
#    module_0.func()