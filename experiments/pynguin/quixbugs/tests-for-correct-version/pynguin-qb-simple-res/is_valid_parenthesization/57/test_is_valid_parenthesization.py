# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import is_valid_parenthesization as module_0


def test_case_0():
    str_0 = "V}7O|a$pw{'P/ksW^~*v"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ""
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is True
    module_0.is_valid_parenthesization(var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "(HF`g6`6L"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False
    module_0.is_valid_parenthesization(var_0)