# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import is_valid_parenthesization as module_0


def test_case_0():
    bytes_0 = b"`D{+\xc7^\xe8\x93`"
    var_0 = module_0.is_valid_parenthesization(bytes_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    var_0 = module_0.is_valid_parenthesization(dict_0)
    assert var_0 is True
    int_0 = -1294
    module_0.is_valid_parenthesization(int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "(p\t\n'z#0"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False
    module_0.is_valid_parenthesization(var_0)