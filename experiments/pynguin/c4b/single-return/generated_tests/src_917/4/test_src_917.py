# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_917 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "0Z\r8+Es-P' %$hP_,du\x0b"
    var_0 = module_0.func(*str_0)
    assert var_0 == "7/6"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "0Z\r8+Es-P' %$hP_,du\x0b"
    var_0 = module_0.func(*str_0)
    assert var_0 == "7/6"
    var_1 = module_0.func(*var_0)
    assert var_1 == "0/1"
    module_0.func()