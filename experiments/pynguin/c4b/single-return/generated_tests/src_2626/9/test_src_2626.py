# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2626 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 204
    set_0 = {int_0, int_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 101
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    int_0 = 204
    set_0 = {int_0, int_0}
    var_1 = module_0.func(*set_0)
    assert var_1 == 101
    module_0.func()