# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import is_valid_parenthesization as module_0
import builtins as module_1


def test_case_0():
    str_0 = "cyqjWZZS04&hqE\t2"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False


def test_case_1():
    list_0 = []
    var_0 = module_0.is_valid_parenthesization(list_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.is_valid_parenthesization(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    list_0 = []
    str_0 = "(h_^kC(Bd&"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False
    object_0 = module_1.object()
    var_1 = module_0.is_valid_parenthesization(list_0)
    assert var_1 is True
    var_2 = module_0.is_valid_parenthesization(list_0)
    assert var_2 is True
    module_0.is_valid_parenthesization(var_1)