# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -1130
    var_0 = module_0.possible_change(int_0, int_0)
    assert var_0 == 0
    var_1 = module_0.possible_change(var_0, var_0)
    assert var_1 == 1
    var_2 = module_0.possible_change(int_0, int_0)
    assert var_2 == 0
    var_3 = module_0.possible_change(int_0, int_0)
    assert var_3 == 0
    var_4 = module_0.possible_change(int_0, var_3)
    assert var_4 == 1
    var_5 = module_0.possible_change(int_0, var_3)
    assert var_5 == 1
    var_6 = module_0.possible_change(var_4, var_3)
    assert var_6 == 1
    var_7 = module_0.possible_change(var_3, int_0)
    assert var_7 == 0
    var_8 = module_0.possible_change(int_0, int_0)
    assert var_8 == 0
    dict_0 = {}
    var_9 = module_0.possible_change(dict_0, int_0)
    assert var_9 == 0
    none_type_0 = None
#    module_0.possible_change(var_8, none_type_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    object_0 = module_1.object()
#    module_0.possible_change(object_0, object_0)


def test_case_2():
    int_0 = -765
    none_type_0 = None
    var_0 = module_0.possible_change(none_type_0, int_0)
    assert var_0 == 0
    var_1 = module_0.possible_change(int_0, int_0)
    assert var_1 == 0
    var_2 = module_0.possible_change(int_0, int_0)
    assert var_2 == 0


#@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 1508.0
#    module_0.possible_change(float_0, float_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    none_type_0 = None
    var_0 = module_0.possible_change(none_type_0, bool_0)
    assert var_0 == 0
#    module_0.possible_change(none_type_0, none_type_0)
