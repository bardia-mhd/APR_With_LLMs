# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2508 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 1612
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x87\x9eR%)"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x87\x9eR%)"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*var_0)
    list_0 = module_0.func(*var_1)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\x1bE\xfa"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*var_1)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_6():
    float_0 = 730.9629592684043
    bool_0 = False
    list_0 = [float_0, float_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*var_1)
    var_3 = module_0.func(*var_0)
    var_4 = module_0.func(*var_1)
    var_5 = module_0.func(*var_3)
    var_6 = module_0.func(*list_0)
    var_7 = module_0.func(*var_4)
    object_0 = module_1.object()
    var_8 = module_0.func(*var_7)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_7():
    bytes_0 = b".\x9eR\xc7u%\xaf"
    var_0 = module_0.func(*bytes_0)
#    module_1.object(*var_0, **var_0)


#@pytest.mark.xfail(strict=True)
def test_case_8():
    bytes_0 = b"OT\xa6T\xfe\x1c"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*var_1)
#    module_1.object(*var_0)