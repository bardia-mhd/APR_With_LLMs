# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2217 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


#@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 635.9872
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    bool_0 = True
    list_1 = [bool_0, bool_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    object_0 = module_1.object()
    bytes_0 = b"<"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "YES"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x07\xc0k\xea\xf3\x95\xd3\x892\x00\x8e0N.q\x11\x17\xc6\xd6"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "YES"
    bool_0 = True
    list_0 = [bool_0, bool_0]
    list_1 = [bool_0, list_0, bool_0, bool_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "NO"
#    module_0.func()