# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import get_factors as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    var_0 = module_0.get_factors(bool_0)
    float_0 = 98.0
    var_1 = module_0.get_factors(float_0)
    var_2 = module_0.get_factors(float_0)
    module_0.get_factors(var_2)


@pytest.mark.xfail(strict=True)
def test_case_1():
    object_0 = module_1.object()
    module_0.get_factors(object_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 675
    var_0 = module_0.get_factors(int_0)
    module_0.get_factors(var_0)