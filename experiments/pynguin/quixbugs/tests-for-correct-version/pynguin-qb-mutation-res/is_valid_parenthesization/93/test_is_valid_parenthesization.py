# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import is_valid_parenthesization as module_0


def test_case_0():
    str_0 = "nKc8!5RI!.l"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False


def test_case_1():
    tuple_0 = ()
    dict_0 = {tuple_0: tuple_0}
    tuple_1 = (tuple_0, dict_0, dict_0)
    var_0 = module_0.is_valid_parenthesization(tuple_1)
    assert var_0 is False
    var_1 = module_0.is_valid_parenthesization(tuple_0)
    assert var_1 is True


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.is_valid_parenthesization(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "(W"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is True
    module_0.is_valid_parenthesization(var_0)