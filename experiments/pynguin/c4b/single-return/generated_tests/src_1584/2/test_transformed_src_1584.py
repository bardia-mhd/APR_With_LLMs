# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1584 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "Jpz+6|T&\x0b=F.I.>k"
    tuple_0 = (str_0, str_0)
    list_0 = [tuple_0, str_0, tuple_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "\\cX,'(4&'|}\"Q`O=4"
    var_0 = module_0.func(*str_0)
    assert var_0 == 1
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    object_0 = module_1.object()
#    module_0.func(*object_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x08\xfb\xd8Z\xdeT{y4\xd21\xac"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 12
    none_type_0 = None
    list_1 = [none_type_0, none_type_0, none_type_0, none_type_0]
#    module_0.func(*list_1)