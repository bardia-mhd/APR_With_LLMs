# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1425 as module_0


def test_case_0():
    float_0 = -638.0
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)


def test_case_1():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"$4H\xce\x1ewo\x9e1"
    var_0 = module_0.func(*bytes_0)
    module_0.func()