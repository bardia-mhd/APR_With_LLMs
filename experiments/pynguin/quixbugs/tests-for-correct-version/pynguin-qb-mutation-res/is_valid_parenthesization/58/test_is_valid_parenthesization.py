# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import is_valid_parenthesization as module_0


def test_case_0():
    bytes_0 = b"\x92\x8b\xb4\t{S?uo\x882\x18'\xb8\"\xbaI"
    var_0 = module_0.is_valid_parenthesization(bytes_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    var_0 = module_0.is_valid_parenthesization(set_0)
    assert var_0 is True
    module_0.is_valid_parenthesization(var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "(vbI"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False
    var_1 = module_0.is_valid_parenthesization(str_0)
    assert var_1 is False
    bool_0 = False
    module_0.is_valid_parenthesization(bool_0)