# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1374 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -3606
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
#    module_0.func(*int_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    bool_1 = False
    list_0 = [bool_0, bool_0, bool_1, bool_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    object_0 = module_1.object()
#    module_0.func(*object_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 472
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()