# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_171 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    dict_0 = {}
    list_0 = [bool_0, dict_0, dict_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -3050
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -3051
    list_0 = [int_0, int_0, int_0]
    module_0.func(*list_0)