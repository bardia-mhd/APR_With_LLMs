# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_281 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "4"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "4"
    bool_0 = False
    tuple_0 = (bool_0, str_0, bool_0, bool_0)
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*tuple_0)
    var_1 = module_0.func(*list_0)
    module_0.func(*bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "4"
    list_0 = [str_0, str_0]
    int_0 = 3007
    list_1 = [int_0, str_0, list_0, str_0]
    var_0 = module_0.func(*list_1)
    module_0.func(*int_0)