# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import quicksort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "y}?f#QNO\x0c5"
    set_0 = {str_0}
    module_0.quicksort(set_0)


def test_case_1():
    bool_0 = False
    var_0 = module_0.quicksort(bool_0)
    var_1 = module_0.quicksort(var_0)
    var_2 = module_0.quicksort(var_0)
    var_3 = module_0.quicksort(var_0)
    var_4 = module_0.quicksort(var_3)
    var_5 = module_0.quicksort(var_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "$-I-5Qk[xQ3o"
    var_0 = module_0.quicksort(str_0)
    var_1 = module_0.quicksort(str_0)
    var_2 = module_0.quicksort(str_0)
    var_3 = module_0.quicksort(var_1)
    int_0 = -1577
    module_0.quicksort(int_0)