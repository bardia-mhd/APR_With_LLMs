# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_156 as module_0


def test_case_0():
    float_0 = 1642.93
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    bool_1 = False
    list_1 = [bool_1, bool_1, bool_1]
    var_1 = module_0.func(*list_1)
    module_0.func()