# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import flatten as module_0
import builtins as module_1


def test_case_0():
    none_type_0 = None
    var_0 = module_0.flatten(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "`<*Dt&f$[SEQym"
    var_0 = module_0.flatten(str_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    set_0 = {bool_0}
    list_0 = [set_0, bool_0, set_0]
    tuple_0 = (bool_0, set_0, list_0, set_0)
    var_0 = module_0.flatten(tuple_0)
    var_1 = module_0.flatten(tuple_0)
    var_2 = module_0.flatten(var_1)
    var_3 = module_0.flatten(set_0)
    var_4 = module_0.flatten(var_3)
    var_5 = module_0.flatten(var_1)
    var_6 = module_0.flatten(tuple_0)
    var_7 = module_0.flatten(var_5)
    var_8 = module_0.flatten(var_3)
    var_9 = module_0.flatten(var_3)
    str_0 = "\\(y}^KzAP4 "
    str_1 = "R$ oF0rCQ"
    dict_0 = {var_4: var_8, str_0: var_5, str_1: var_9}
    module_1.object(*var_2, **dict_0)