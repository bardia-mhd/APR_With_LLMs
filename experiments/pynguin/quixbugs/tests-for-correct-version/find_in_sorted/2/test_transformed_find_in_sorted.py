# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_in_sorted as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = ";UoXY*oZ]"
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1
#    module_0.find_in_sorted(var_0, str_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    dict_0 = {bool_0: bool_0}
    str_0 = "I389>^l"
    list_0 = [dict_0, dict_0, str_0]
    none_type_0 = None
#    module_0.find_in_sorted(list_0, none_type_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    none_type_0 = None
#    module_0.find_in_sorted(bool_0, none_type_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "m"
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == 0
    none_type_0 = None
#    module_0.find_in_sorted(none_type_0, none_type_0)
