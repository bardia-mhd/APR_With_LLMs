# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1519 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 473.95
    set_0 = {float_0, float_0}
    var_0 = module_0.func(*set_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xe7\x07I\xf5E3\xde\xfd\x88"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()