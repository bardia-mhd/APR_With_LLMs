# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_804 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 276.93
    list_0 = [float_0, float_0, float_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "mvg\x0b?/(E"
    var_0 = module_0.func(*str_0)
    assert var_0 == 2
    module_0.func()