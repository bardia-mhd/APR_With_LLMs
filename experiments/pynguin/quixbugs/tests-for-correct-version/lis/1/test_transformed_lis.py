# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1084
    set_0 = {int_0}
    var_0 = module_0.lis(set_0)
    assert var_0 == 1
#    module_0.lis(var_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = 'd)2(3]"vLjGE`SP]R]Jp'
    var_0 = module_0.lis(str_0)
    assert var_0 == 8
#    module_0.lis(var_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    complex_0 = 416.133017 + 1479.750442j
#    module_0.lis(complex_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "VFc;"
    list_0 = [str_0, str_0]
    var_0 = module_0.lis(list_0)
    assert var_0 == 1
#    module_0.lis(var_0)
