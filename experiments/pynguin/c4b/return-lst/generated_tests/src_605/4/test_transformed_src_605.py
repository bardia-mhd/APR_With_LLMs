# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_605 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "64e\x0cM"
    list_0 = [str_0]
#    module_0.func(*list_0)


def test_case_1():
    str_0 = "690"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "690e*"
    list_0 = [str_0, str_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "60+9"
    list_0 = [str_0, str_0]
#    module_0.func(*list_0)


def test_case_5():
    str_0 = "06909"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)