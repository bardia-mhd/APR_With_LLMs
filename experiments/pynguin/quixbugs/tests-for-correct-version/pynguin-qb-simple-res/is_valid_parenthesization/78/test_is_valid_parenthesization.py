# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import is_valid_parenthesization as module_0


def test_case_0():
    str_0 = "Mqw_E"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b""
    var_0 = module_0.is_valid_parenthesization(bytes_0)
    assert var_0 is True
    module_0.is_valid_parenthesization(var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.is_valid_parenthesization(none_type_0)


def test_case_3():
    str_0 = "(o(d|zpp"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False
    str_1 = "Mqw_E"
    var_1 = module_0.is_valid_parenthesization(str_1)
    assert var_1 is False