# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_806 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    float_0 = 859.8466
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0, none_type_0, none_type_0]
    bytes_0 = b"\x02N:%C"
    var_0 = module_0.func(*bytes_0)
#    module_0.func(*list_0)