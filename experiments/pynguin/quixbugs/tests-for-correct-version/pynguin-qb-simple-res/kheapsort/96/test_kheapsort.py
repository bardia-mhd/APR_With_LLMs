# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kheapsort as module_0
import builtins as module_1


def test_case_0():
    int_0 = 890
    tuple_0 = (int_0,)
    var_0 = module_0.kheapsort(tuple_0, int_0)


def test_case_1():
    list_0 = []
    none_type_0 = None
    var_0 = module_0.kheapsort(list_0, none_type_0)
    object_0 = module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -1166.5258
    tuple_0 = ()
    var_0 = module_0.kheapsort(float_0, tuple_0)
    var_1 = module_0.kheapsort(float_0, tuple_0)
    list_0 = [float_0, float_0, float_0, float_0]
    none_type_0 = None
    bool_0 = True
    var_2 = module_0.kheapsort(list_0, bool_0)
    var_3 = module_0.kheapsort(none_type_0, var_1)
    var_4 = module_0.kheapsort(none_type_0, none_type_0)
    var_5 = module_0.kheapsort(none_type_0, var_2)
    var_6 = module_0.kheapsort(var_2, none_type_0)
    var_7 = module_0.kheapsort(var_3, list_0)
    var_8 = module_0.kheapsort(var_3, var_4)
    var_9 = module_0.kheapsort(list_0, float_0)
    list_1 = []
    var_10 = module_0.kheapsort(list_1, float_0)
    var_11 = module_0.kheapsort(var_3, var_3)
    var_12 = module_0.kheapsort(none_type_0, var_4)
    none_type_1 = None
    var_13 = module_0.kheapsort(var_1, float_0)
    var_14 = module_0.kheapsort(tuple_0, list_0)
    var_15 = module_0.kheapsort(var_14, var_7)
    var_16 = module_0.kheapsort(var_12, var_1)
    var_17 = module_0.kheapsort(var_4, none_type_0)
    var_18 = module_0.kheapsort(var_14, var_1)
    var_19 = module_0.kheapsort(list_0, none_type_1)
    set_0 = {bool_0, var_11}
    var_20 = module_0.kheapsort(var_1, set_0)
    bool_1 = True
    var_21 = module_0.kheapsort(bool_1, var_4)
    module_1.object(*var_19)