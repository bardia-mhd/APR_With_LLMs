# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_553 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "n9x\t!4c#5 1&\x0ca;;Bx"
    var_0 = module_0.func(*str_0)
    assert var_0 == 2


def test_case_2():
    str_0 = "n9x\t!4c#5 1&\x0ca;;Bx"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 19


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ".^2\x0cf(Eq15U>_T"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 7
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ""
    list_0 = [str_0]
    module_0.func(*list_0)