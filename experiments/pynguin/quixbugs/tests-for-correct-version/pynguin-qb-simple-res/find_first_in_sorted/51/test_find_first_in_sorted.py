# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_first_in_sorted as module_0
import builtins as module_1


def test_case_0():
    str_0 = '.`jJgt*LA(T"6e%33'
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.find_first_in_sorted(tuple_0, tuple_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "U"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == 0
    module_0.find_first_in_sorted(str_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -2681
    list_0 = [int_0, int_0]
    var_0 = module_0.find_first_in_sorted(list_0, int_0)
    assert var_0 == 0
    module_0.find_first_in_sorted(int_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    set_0 = {bool_0, bool_0, bool_0}
    bool_1 = False
    str_0 = ""
    tuple_0 = (set_0, bool_0, bool_1, str_0)
    var_0 = module_0.find_first_in_sorted(tuple_0, bool_1)
    assert var_0 == 1
    int_0 = -2681
    list_0 = [int_0, int_0]
    module_1.object(*list_0)