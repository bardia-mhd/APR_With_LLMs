# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1701 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 4
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -3370
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    none_type_0 = None
    list_1 = [none_type_0, none_type_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*list_0)
    var_3 = module_0.func(*var_2)
    var_4 = module_0.func(*var_3)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 4
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*var_1)
    list_1 = []
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 5
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    bool_0 = True
    list_1 = [bool_0, bool_0, bool_0, bool_0]
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*list_1)
    var_3 = module_0.func(*var_2)
    var_4 = module_0.func(*var_3)
#    module_1.object(*var_2, **var_4)