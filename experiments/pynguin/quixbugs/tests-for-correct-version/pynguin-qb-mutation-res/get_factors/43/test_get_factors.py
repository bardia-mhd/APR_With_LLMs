# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import get_factors as module_0


def test_case_0():
    bool_0 = True
    var_0 = module_0.get_factors(bool_0)
    var_1 = module_0.get_factors(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    complex_0 = -1588.58665 - 415.357j
    module_0.get_factors(complex_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    var_0 = module_0.get_factors(bool_0)
    int_0 = 1632
    var_1 = module_0.get_factors(int_0)
    module_0.get_factors(var_1)