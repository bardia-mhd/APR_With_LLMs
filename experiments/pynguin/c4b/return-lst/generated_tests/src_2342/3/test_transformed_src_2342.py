# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2342 as module_0


def test_case_0():
    str_0 = "0;0"
    var_0 = module_0.func(*str_0)


def test_case_1():
    set_0 = set()
    list_0 = [set_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


def test_case_3():
    bytes_0 = b"2\xf9\xcb\x87\x9f\xfa\xff"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


def test_case_4():
    str_0 = "RH["
    var_0 = module_0.func(*str_0)


def test_case_5():
    str_0 = "1H["
    var_0 = module_0.func(*str_0)


def test_case_6():
    str_0 = "@6000111>1111"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "00`0000401"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    var_2 = module_0.func(*var_0)
#    module_0.func()