# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_first_in_sorted as module_0


def test_case_0():
    list_0 = []
    list_1 = [list_0, list_0, list_0]
    var_0 = module_0.find_first_in_sorted(list_1, list_0)
    assert var_0 == 0


def test_case_1():
    str_0 = ""
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.find_first_in_sorted(bool_0, bool_0)


def test_case_3():
    bool_0 = False
    list_0 = [bool_0]
    float_0 = 2550.56
    var_0 = module_0.find_first_in_sorted(list_0, float_0)
    assert var_0 == -1


def test_case_4():
    list_0 = []
    list_1 = [list_0, list_0, list_0]
    var_0 = module_0.find_first_in_sorted(list_1, list_1)
    assert var_0 == -1
    var_1 = module_0.find_first_in_sorted(list_1, list_0)
    assert var_1 == 0
    list_2 = [list_1, var_1]
    var_2 = module_0.find_first_in_sorted(list_2, var_1)
    assert var_2 == 1