# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -2326
    var_0 = module_0.possible_change(int_0, int_0)
    assert var_0 == 0
    var_1 = module_0.possible_change(int_0, int_0)
    assert var_1 == 0
    var_2 = module_0.possible_change(var_1, var_1)
    assert var_2 == 1
    object_0 = module_1.object()
    var_3 = module_0.possible_change(var_2, int_0)
    assert var_3 == 0
    var_4 = module_0.possible_change(var_1, var_1)
    assert var_4 == 1
    none_type_0 = None
    module_0.possible_change(object_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "\n"
    module_0.possible_change(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -2276.941795
    var_0 = module_0.possible_change(float_0, float_0)
    assert var_0 == 0
    str_0 = "V|"
    module_0.possible_change(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 157
    module_0.possible_change(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 2101
    none_type_0 = None
    var_0 = module_0.possible_change(none_type_0, int_0)
    assert var_0 == 0
    var_1 = module_0.possible_change(none_type_0, int_0)
    assert var_1 == 0
    float_0 = 823.3
    var_2 = module_0.possible_change(var_1, float_0)
    assert var_2 == 0
    module_0.possible_change(int_0, int_0)