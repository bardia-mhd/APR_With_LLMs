# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import is_valid_parenthesization as module_0


def test_case_0():
    str_0 = ",)?w]\\c&!sKu%u"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    list_0 = module_0.is_valid_parenthesization(dict_0)
    assert list_0 is True
    module_0.is_valid_parenthesization(list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.is_valid_parenthesization(none_type_0)


def test_case_3():
    str_0 = "(x(r~\\"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False