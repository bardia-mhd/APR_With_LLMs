# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_in_sorted as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "-m!WgHYzN"
    str_1 = ',Is2"'
    var_0 = module_0.find_in_sorted(str_1, str_0)
    assert var_0 == -1
#    module_1.object(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b'\xa4\xbd"~\xb4J\x9a>{'
    none_type_0 = None
#    module_0.find_in_sorted(bytes_0, none_type_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 33.453267
#    module_0.find_in_sorted(float_0, float_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    str_0 = "x"
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == 0
#    module_0.find_in_sorted(bool_0, bool_0)
