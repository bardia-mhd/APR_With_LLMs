# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2007 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -1478.928
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -1478.5984550383907
    list_0 = [float_0, float_0, float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    set_0 = {bool_0, bool_0, bool_0}
    list_0 = [bool_0, bool_0, set_0, set_0]
    var_0 = module_0.func(*list_0)
    module_0.func()