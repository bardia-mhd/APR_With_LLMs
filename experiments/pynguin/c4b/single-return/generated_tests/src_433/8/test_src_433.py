# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_433 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "4U@"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = '8QP{G#j)Jg["'
    var_0 = module_0.func(*str_0)
    assert var_0 == 1
    module_0.func()