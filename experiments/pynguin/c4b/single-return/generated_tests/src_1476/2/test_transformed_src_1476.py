# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1476 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 522
    bool_0 = False
    list_0 = [int_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 105
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 1158.889
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 232
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 549
    bool_0 = False
    list_0 = [int_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 110
    var_1 = module_1.object()
#    module_0.func(*var_1)