# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_first_in_sorted as module_0
import builtins as module_1


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.find_first_in_sorted(list_0, bool_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ""
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1
    var_1 = module_0.find_first_in_sorted(str_0, var_0)
    assert var_1 == -1
    bool_0 = True
    none_type_0 = None
    module_0.find_first_in_sorted(bool_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.find_first_in_sorted(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    module_0.find_first_in_sorted(list_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.find_first_in_sorted(list_0, bool_0)
    assert var_0 == 0
    var_1 = module_0.find_first_in_sorted(list_0, var_0)
    assert var_1 == -1
    object_0 = module_1.object()
    module_0.find_first_in_sorted(object_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "%D"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1
    module_0.find_first_in_sorted(var_0, var_0)


def test_case_6():
    bool_0 = False
    float_0 = -2141.14
    set_0 = {float_0, bool_0, bool_0, bool_0}
    tuple_0 = (set_0,)
    tuple_1 = (bool_0, float_0, tuple_0)
    var_0 = module_0.find_first_in_sorted(tuple_1, float_0)
    assert var_0 == 1