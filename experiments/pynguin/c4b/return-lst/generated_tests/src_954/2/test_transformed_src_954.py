# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_954 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    bool_0 = True
    set_0 = {bool_0, bool_0}
    var_0 = module_0.func(*set_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 4314.6799
    set_0 = {float_0, float_0, float_0, float_0}
    var_0 = module_0.func(*set_0)
    bool_0 = True
    list_0 = [bool_0]
    var_1 = module_0.func(*list_0)
#    module_0.func()