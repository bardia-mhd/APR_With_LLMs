# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1761 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xcc\xb7\xe5\xfa\xacF\xdd6\x03\xd6\xac"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 1
    object_0 = module_1.object()
    complex_0 = -1434.945239 - 781.665j
    list_1 = [bool_0, bool_0, complex_0]
    var_2 = module_0.func(*list_1)
    assert var_2 == 1
#    module_0.func()