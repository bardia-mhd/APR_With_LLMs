# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1099 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -1078
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "-1:20"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 1527
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "16:34"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -1806
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "-1:00"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 2970
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "06:30"
    module_0.func()