# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1609 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    float_0 = -170.87758979621586
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x04 *\x14\x8bD\xf5\xfc\xebyN\xa4F\xf1g\x14\xe6\xe2Ic"
    var_0 = module_0.func(*bytes_0)
    float_0 = -35.97592489200412
    list_0 = [float_0, float_0, float_0, float_0]
    var_1 = module_0.func(*list_0)
    object_0 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x07\xe4?\xde)#\xe11"
    var_0 = module_0.func(*bytes_0)
    float_0 = -100.51085804284534
    list_0 = [float_0, float_0, float_0, float_0]
    var_1 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xe4?\xde#\xe11"
    var_0 = module_0.func(*bytes_0)
    float_0 = -63.69074662135141
    list_0 = [float_0, float_0, float_0, float_0]
    var_1 = module_0.func(*list_0)
    module_0.func(*var_1)