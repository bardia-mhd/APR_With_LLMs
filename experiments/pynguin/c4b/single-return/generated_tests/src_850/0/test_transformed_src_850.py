# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_850 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    set_0 = {bool_0, bool_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == "Sheldon"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 1154
    dict_0 = {int_0: int_0, int_0: int_0}
    list_0 = [int_0, dict_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Howard"
    var_1 = module_0.func(*list_0)
    assert var_1 == "Howard"
#    module_0.func()