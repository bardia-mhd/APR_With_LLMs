# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import src_1715 as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -1273.61
    object_0 = module_0.object()
    list_0 = [float_0, float_0, float_0]
    var_0 = module_1.func(*list_0)
    assert var_0 == -849
    module_1.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_1.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 831.6954719313784
    list_0 = [float_0, float_0]
    var_0 = module_1.func(*list_0)
    assert var_0 == 554
    module_1.func()