# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2295 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    str_0 = "h?+[]"
    bytes_0 = b"\x02e8\xf5\x91\xdb"
    tuple_0 = (bool_0, str_0, bool_0, bytes_0)
    set_0 = {bool_0, tuple_0, bytes_0}
    list_0 = [tuple_0, set_0, bytes_0, str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()