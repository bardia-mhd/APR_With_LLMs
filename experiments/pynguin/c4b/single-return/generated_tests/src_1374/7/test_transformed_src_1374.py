# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1374 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1398
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 349
#    module_1.object(**var_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 1393
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    list_1 = [int_0, int_0, int_0, int_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -3368
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -843
#    module_0.func()