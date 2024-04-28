# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_in_sorted as module_0


def test_case_0():
    bytes_0 = b""
    none_type_0 = None
    var_0 = module_0.find_in_sorted(bytes_0, none_type_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    module_0.find_in_sorted(dict_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.find_in_sorted(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "6d{?["
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1
    var_1 = module_0.find_in_sorted(str_0, str_0)
    assert var_1 == -1
    module_0.find_in_sorted(var_1, var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = '"'
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == 0
    str_1 = "6d{?["
    var_1 = module_0.find_in_sorted(str_1, str_1)
    assert var_1 == -1
    int_0 = 933
    bool_0 = False
    list_0 = [int_0, var_0, str_0, bool_0]
    module_0.find_in_sorted(var_1, list_0)