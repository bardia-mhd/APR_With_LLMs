# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_819 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 495.0
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"9y\x98\x02\x92\xc4\x9aW\xef\\\x8d\xd4\xab\xec2 "
    var_0 = module_0.func(*bytes_0)
    bool_0 = False
    var_1 = module_0.func(*var_0)
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_2 = module_0.func(*list_0)
#    module_0.func()