# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2007 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 4246.236
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert (
        var_0
        == "4777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777"
    )
    module_0.func()


def test_case_1():
    float_0 = -441.5923
    object_0 = module_1.object()
    list_0 = [float_0, float_0, object_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -1
    list_1 = [float_0, float_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == -1


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()