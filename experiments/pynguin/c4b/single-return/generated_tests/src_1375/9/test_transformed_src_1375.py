# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1375 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 7670.534
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Penny"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -93.3835
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Sheldon"
#    module_0.func()