# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2575 as module_0


def test_case_0():
    str_0 = "VaG1K!F4e=`5Cd"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "VVaG1K!F4e=`5Cd"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    str_0 = "~B-RKK;G?]CcTJT?$lx"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)