# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1299 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "11*4/M>90n"
    var_0 = module_0.func(*str_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "62W^NU/^{XVG<7"
    module_0.func(*str_0)


def test_case_3():
    str_0 = "0 :wb'@tAq [(Z@2"
    var_0 = module_0.func(*str_0)
    assert var_0 == 7