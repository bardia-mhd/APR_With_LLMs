# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2189 as module_0


def test_case_0():
    bytes_0 = b"\x13"
    var_0 = module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    int_0 = 464
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b'\x14\xc2\xcd\x1a\xcdWmB%\x89\xec"\x83\xea\xfb>\xf6\xe5'
    var_0 = module_0.func(*bytes_0)
    int_0 = -2238
    list_0 = [int_0]
    var_1 = module_0.func(*list_0)
#    module_0.func()