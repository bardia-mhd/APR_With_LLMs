# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import hanoi as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 3581
    module_0.hanoi(int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    var_0 = module_0.hanoi(bool_0)
    int_0 = -1633
    var_1 = module_0.hanoi(int_0, end=int_0)
    module_0.hanoi(var_0)