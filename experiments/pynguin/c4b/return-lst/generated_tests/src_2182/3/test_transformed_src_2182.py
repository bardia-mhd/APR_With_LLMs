# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2182 as module_0


def test_case_0():
    bytes_0 = b"\xfb\x16\xbb\xe3\x8a\x89\xffPJ\x84\xf3E"
    var_0 = module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = "9"
    var_0 = module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 15
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 20
    list_0 = [int_0, int_0, int_0, int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    var_2 = module_0.func(*var_1)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 10
    list_0 = [int_0, int_0, int_0, int_0, int_0]
#    module_0.func(*list_0)