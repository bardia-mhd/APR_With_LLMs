# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1587 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    bytes_0 = b"\x1b\x81\xfb\xf2F\x9c\xf4\xf5l\x1f\xc7\x89\x8b#\xf5\x9b\xa9n;p"
    var_0 = module_0.func(*bytes_0)
    list_0 = [none_type_0, none_type_0, none_type_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()