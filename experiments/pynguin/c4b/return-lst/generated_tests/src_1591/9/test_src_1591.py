# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1591 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    set_0 = {bool_0}
    list_0 = [bool_0, set_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    set_0 = set()
    list_0 = [bool_0, set_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "61w~l*^ja}$,]"
    var_0 = module_0.func(*str_0)
    tuple_0 = (var_0, var_0, str_0, var_0)
    list_0 = [tuple_0]
    module_0.func(*list_0)