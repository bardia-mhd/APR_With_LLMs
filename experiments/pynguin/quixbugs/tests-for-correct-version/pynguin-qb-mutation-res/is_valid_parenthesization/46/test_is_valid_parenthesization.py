# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import is_valid_parenthesization as module_0


def test_case_0():
    bytes_0 = b"\xc3\xdf>x\x1d1[\xb4\x0e\xda\x1c\xca%1\xffu\xd0\xd6K\x12"
    var_0 = module_0.is_valid_parenthesization(bytes_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b""
    var_0 = module_0.is_valid_parenthesization(bytes_0)
    assert var_0 is True
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_1 = module_0.is_valid_parenthesization(list_0)
    assert var_1 is False
    var_2 = module_0.is_valid_parenthesization(list_0)
    assert var_2 is False
    var_3 = module_0.is_valid_parenthesization(list_0)
    assert var_3 is False
    var_4 = module_0.is_valid_parenthesization(list_0)
    assert var_4 is False
    module_0.is_valid_parenthesization(var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "(=F~5X-Jlu*'"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False
    none_type_0 = None
    module_0.is_valid_parenthesization(none_type_0)