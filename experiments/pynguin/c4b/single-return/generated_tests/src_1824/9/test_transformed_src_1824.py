# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1824 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b'\xc2"\xe0\x010D'
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


#@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
#    module_0.func(*none_type_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xf0>x\xffH\xdb\xc5\x16\xb4\x00\xe5,\xcc\xf5\x87&c"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    object_0 = module_1.object()
#    module_0.func(*object_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0, bool_0, bool_0, bool_0]
    dict_0 = {}
    list_1 = [list_0, dict_0, dict_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "YES"
#    module_0.func(*var_0)