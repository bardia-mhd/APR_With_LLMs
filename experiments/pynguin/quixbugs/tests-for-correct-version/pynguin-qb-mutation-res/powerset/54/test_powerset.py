# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import powerset as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    object_0 = module_0.object()
    module_1.powerset(object_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    var_0 = module_1.powerset(bool_0)
    float_0 = 4123.64
    module_1.powerset(float_0)


def test_case_2():
    bytes_0 = b""
    set_0 = {bytes_0}
    var_0 = module_1.powerset(set_0)
    bytes_1 = b"I\x03\x03\x835"
    var_1 = module_1.powerset(bytes_1)