# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_263 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "d)m U--S\nH_MCQQ"
    var_0 = module_0.func(*str_0)
    assert var_0 == 2
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -1495
#    module_0.func(*int_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "Yr$(reo.=$Y:T"
    var_0 = module_0.func(*str_0)
    assert var_0 == 1
    var_1 = module_0.func(*str_0)
    assert var_1 == 1
#    module_0.func()