# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import is_valid_parenthesization as module_0


def test_case_0():
    set_0 = set()
    list_0 = [set_0, set_0]
    var_0 = module_0.is_valid_parenthesization(list_0)
    assert var_0 is False


def test_case_1():
    dict_0 = {}
    var_0 = module_0.is_valid_parenthesization(dict_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_2():
    tuple_0 = ()
    var_0 = module_0.is_valid_parenthesization(tuple_0)
    assert var_0 is True
    str_0 = "(}+^?*I/h_lHvDv/It\tc"
    var_1 = module_0.is_valid_parenthesization(str_0)
    assert var_1 is False
    var_2 = module_0.is_valid_parenthesization(str_0)
    assert var_2 is False
    int_0 = -1080
    module_0.is_valid_parenthesization(int_0)