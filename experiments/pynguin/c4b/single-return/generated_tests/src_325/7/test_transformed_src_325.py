# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_325 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = True
    dict_0 = {
        bool_0: bool_0,
        bool_0: bool_0,
        bool_0: bool_0,
        bool_0: bool_0,
        bool_0: bool_0,
    }
    list_0 = [bool_0, dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    list_0 = [bool_0, dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    object_0 = module_1.object()
    object_1 = module_1.object()
    list_1 = [bool_0, list_0, object_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    list_0 = [bool_0, dict_0, dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    int_0 = 3406
    list_1 = [int_0, list_0, list_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 1
#    module_0.func()