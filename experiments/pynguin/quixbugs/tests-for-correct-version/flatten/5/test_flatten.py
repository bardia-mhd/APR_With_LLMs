# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import flatten as module_0
import builtins as module_1


def test_case_0():
    bool_0 = False
    var_0 = module_0.flatten(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "^<\r0b\n+ldk"
    var_0 = module_0.flatten(str_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    var_0 = module_0.flatten(none_type_0)
    dict_0 = {}
    list_0 = []
    tuple_0 = (dict_0, dict_0, list_0)
    var_1 = module_0.flatten(tuple_0)
    var_2 = module_0.flatten(var_1)
    module_1.object(*var_2)


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    var_0 = module_0.flatten(none_type_0)
    dict_0 = {}
    list_0 = [dict_0]
    tuple_0 = (dict_0, dict_0, list_0)
    var_1 = module_0.flatten(tuple_0)
    var_2 = module_0.flatten(var_1)
    module_1.object(*var_2)