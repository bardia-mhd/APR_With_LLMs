# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import is_valid_parenthesization as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"@\xbes\x0b[\xb6\\-hp\x13\xd8\x15\x8e\xa6\xc8\x0f\x1e\xee\xa2"
    var_0 = module_0.is_valid_parenthesization(bytes_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "("
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False
    str_1 = "/IWGeY=[[\x0c"
    var_1 = module_0.is_valid_parenthesization(str_1)
    assert var_1 is False
    module_0.is_valid_parenthesization(var_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "(/"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is True
    bytes_0 = b"@\xbes\x0b&2\xf5\xa9hp\xef\xd8\x15\x8e\xa6\xc8\x0f\x1et\xa2"
    var_1 = module_0.is_valid_parenthesization(bytes_0)
    assert var_1 is False
    var_2 = module_0.is_valid_parenthesization(str_0)
    assert var_2 is True
    var_3 = module_1.object()
    module_0.is_valid_parenthesization(var_2)