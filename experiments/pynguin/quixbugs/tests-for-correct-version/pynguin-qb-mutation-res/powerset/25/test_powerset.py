# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import powerset as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    complex_0 = -970.46 + 394.403943j
    module_0.powerset(complex_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.powerset(none_type_0)
    var_1 = module_0.powerset(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "3MJ5N"
    str_1 = "_[\tNz#kDjI"
    var_0 = module_0.powerset(str_1)
    var_1 = module_0.powerset(str_0)
    int_0 = 1891
    module_0.powerset(int_0)