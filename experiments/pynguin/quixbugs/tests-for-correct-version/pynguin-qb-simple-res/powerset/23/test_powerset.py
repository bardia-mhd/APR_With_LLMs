# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import powerset as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -1588
    module_0.powerset(int_0)


def test_case_1():
    int_0 = 2304
    set_0 = {int_0}
    var_0 = module_0.powerset(set_0)