# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1715 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = 666.5
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 645.3969334193451
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_0.func(*var_0)
#    module_1.object(*list_0)