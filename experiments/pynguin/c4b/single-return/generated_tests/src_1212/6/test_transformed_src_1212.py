# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1212 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "z5</8]n"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "Z-"
    var_0 = module_0.func(*str_0)
    assert var_0 == "YES"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "u5"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    list_0 = []
    list_1 = [list_0, list_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "NO"
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    list_2 = [dict_0, dict_0]
    var_1 = module_0.func(*list_2)
    assert var_1 == "YES"
#    module_0.func()