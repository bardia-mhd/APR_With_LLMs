# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import flatten as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -404
    tuple_0 = (int_0, int_0)
    var_0 = module_0.flatten(tuple_0)
    var_1 = module_0.flatten(int_0)
    var_2 = module_0.flatten(tuple_0)
    var_3 = module_0.flatten(var_0)
    var_4 = module_0.flatten(var_2)
    str_0 = ".S\x0b2X]I"
    dict_0 = {var_0: var_4, str_0: var_1}
    module_1.object(*var_2, **dict_0)


def test_case_1():
    int_0 = 2883
    var_0 = module_0.flatten(int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -404
    list_0 = []
    var_0 = module_0.flatten(int_0)
    tuple_0 = (int_0, list_0)
    var_1 = module_0.flatten(var_0)
    var_2 = module_0.flatten(int_0)
    var_3 = module_0.flatten(tuple_0)
    var_4 = module_0.flatten(var_1)
    var_5 = module_0.flatten(var_3)
    str_0 = ".S\x0b2X]I"
    dict_0 = {var_1: var_5, str_0: var_2}
    var_6 = module_0.flatten(var_1)
    module_1.object(*var_3, **dict_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -404
    list_0 = [int_0, int_0]
    tuple_0 = (int_0, list_0)
    var_0 = module_0.flatten(int_0)
    var_1 = module_0.flatten(var_0)
    var_2 = module_0.flatten(var_0)
    var_3 = module_0.flatten(int_0)
    var_4 = module_0.flatten(tuple_0)
    var_5 = module_0.flatten(var_2)
    var_6 = module_0.flatten(var_4)
    str_0 = ".S\x0b2X]I"
    var_7 = module_0.flatten(list_0)
    dict_0 = {var_2: var_6, str_0: var_3}
    module_1.object(*var_4, **dict_0)