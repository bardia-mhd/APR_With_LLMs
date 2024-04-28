# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_first_in_sorted as module_0
import builtins as module_1


def test_case_0():
    str_0 = '"&rO}\t"+'
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    var_0 = module_0.find_first_in_sorted(dict_0, dict_0)
    assert var_0 == -1
    list_0 = []
    var_1 = module_0.find_first_in_sorted(list_0, list_0)
    assert var_1 == -1
    module_0.find_first_in_sorted(var_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.find_first_in_sorted(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "M"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == 0
    module_1.object(**var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    int_0 = 515
    list_1 = [bool_0, list_0, int_0]
    var_0 = module_0.find_first_in_sorted(list_1, list_0)
    assert var_0 == 1
    module_1.object(*list_1, **var_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.find_first_in_sorted(list_0, bool_0)
    assert var_0 == 0
    int_0 = 515
    list_1 = [bool_0, list_0, int_0]
    var_1 = module_0.find_first_in_sorted(list_1, list_0)
    assert var_1 == 1
    module_0.find_first_in_sorted(var_1, list_1)