# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import flatten as module_0
import builtins as module_1


def test_case_0():
    float_0 = 3001.089269
    var_0 = module_0.flatten(float_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "=-@U"
    var_0 = module_0.flatten(str_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    dict_0 = {}
    list_1 = [list_0, list_0, bool_0, dict_0]
    var_0 = module_0.flatten(list_0)
    var_1 = module_0.flatten(list_1)
    var_2 = module_0.flatten(var_0)
    none_type_0 = None
    var_3 = module_0.flatten(var_1)
    var_4 = module_0.flatten(none_type_0)
    var_5 = module_0.flatten(var_1)
    var_6 = module_0.flatten(none_type_0)
    var_7 = module_0.flatten(var_1)
    module_1.object(*var_7)