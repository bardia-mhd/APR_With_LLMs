# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import is_valid_parenthesization as module_0


def test_case_0():
    str_0 = "Rn+"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x88\x1d\x1cQ=\xbb\x87\x99\xca*\xfa/\x10\x8d~h\\z"
    var_0 = module_0.is_valid_parenthesization(bytes_0)
    assert var_0 is False
    set_0 = set()
    var_1 = module_0.is_valid_parenthesization(set_0)
    assert var_1 is True
    module_0.is_valid_parenthesization(var_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.is_valid_parenthesization(bool_0)


def test_case_3():
    str_0 = "(1>"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False