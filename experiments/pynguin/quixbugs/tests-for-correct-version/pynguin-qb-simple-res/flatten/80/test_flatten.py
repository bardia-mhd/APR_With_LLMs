# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import flatten as module_0
import builtins as module_1


def test_case_0():
    bool_0 = True
    var_0 = module_0.flatten(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ")_\"']^O"
    var_0 = module_0.flatten(str_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    bool_1 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_1, bool_1: bool_0}
    list_0 = [dict_0, bool_1, bool_0]
    var_0 = module_0.flatten(list_0)
    none_type_0 = None
    var_1 = module_0.flatten(list_0)
    var_2 = module_0.flatten(var_0)
    int_0 = -578
    var_3 = module_0.flatten(int_0)
    set_0 = {int_0}
    var_4 = module_0.flatten(set_0)
    var_5 = module_0.flatten(var_4)
    var_6 = module_0.flatten(dict_0)
    var_7 = module_0.flatten(none_type_0)
    var_8 = module_0.flatten(var_7)
    var_9 = module_0.flatten(var_5)
    var_10 = module_0.flatten(var_9)
    var_11 = module_0.flatten(var_8)
    var_12 = module_0.flatten(var_7)
    var_13 = module_0.flatten(var_5)
    var_14 = module_0.flatten(var_5)
    var_15 = module_0.flatten(bool_0)
    var_16 = module_0.flatten(set_0)
    var_17 = module_0.flatten(var_4)
    var_18 = module_0.flatten(var_8)
    var_19 = module_0.flatten(var_16)
    var_20 = module_0.flatten(var_11)
    list_1 = [var_1, int_0, list_0, var_14]
    var_21 = module_0.flatten(list_1)
    module_1.object(*var_21)