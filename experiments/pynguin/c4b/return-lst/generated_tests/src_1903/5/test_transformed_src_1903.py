# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1903 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"\x052\x8a\x88\xd7\xc0f[\xe62\x1f\x1dFSD\x9c"
    set_0 = {bytes_0, bytes_0}
    tuple_0 = (bytes_0, bytes_0, bytes_0, set_0)
    list_0 = [tuple_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    bytes_0 = b"\xcf\x9d\xb3\xf0\r<\xb74\xb8b\xba"
    set_0 = set()
    list_0 = [
        set_0,
        set_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        set_0,
        set_0,
    ]
    list_1 = [list_0, set_0, bytes_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xcf\x9d\xb3\xf0\r<\xb74\xb8b\xba"
    set_0 = set()
    tuple_0 = (bytes_0, bytes_0, bytes_0, set_0)
    list_0 = [
        set_0,
        set_0,
        tuple_0,
        tuple_0,
        tuple_0,
        tuple_0,
        tuple_0,
        tuple_0,
        tuple_0,
        set_0,
        tuple_0,
        set_0,
    ]
    list_1 = [list_0, set_0, bytes_0]
    var_0 = module_1.object()
    var_1 = module_0.func(*list_1)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "$BB_,Mz>_stT4"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    list_1 = [list_0]
    var_1 = module_0.func(*list_0)
    var_2 = module_0.func(*list_1)
    object_0 = module_1.object()
#    module_0.func()