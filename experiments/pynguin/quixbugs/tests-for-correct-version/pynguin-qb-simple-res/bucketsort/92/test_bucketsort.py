# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bucketsort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 745
    int_1 = 1074
    list_0 = [int_0, int_0, int_0, int_1, int_1, int_1, int_1]
    module_0.bucketsort(list_0, int_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    module_0.bucketsort(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 773
    int_1 = 1070
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.bucketsort(list_0, int_1)
    module_0.bucketsort(int_0, list_0)