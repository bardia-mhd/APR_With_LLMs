# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_466 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "88"
    bytes_0 = b"]"
    tuple_0 = (str_0, bytes_0, str_0, bytes_0)
#    module_0.func(*tuple_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "1"
    bytes_0 = b"\xf0"
    tuple_0 = (str_0, bytes_0, str_0, bytes_0)
    var_0 = module_0.func(*tuple_0)
    object_0 = module_1.object()
    list_0 = [object_0, object_0, object_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "1"
    int_0 = -2836
    list_0 = [str_0, str_0, int_0]
    var_0 = module_0.func(*list_0)
    bytes_0 = b"\xf0"
    tuple_0 = (str_0, bytes_0, str_0, bytes_0)
    var_1 = module_0.func(*tuple_0)
    object_0 = module_1.object()
    list_1 = [object_0, object_0, object_0]
#    module_0.func(*list_1)