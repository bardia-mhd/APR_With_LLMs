# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_in_sorted as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "F_I>o\tL?;ED1%vs}t"
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1
    none_type_0 = None
#    module_0.find_in_sorted(none_type_0, str_0)


def test_case_1():
    complex_0 = -2305.4 + 3284.7399j
    set_0 = {complex_0}
    tuple_0 = (set_0,)
    var_0 = module_0.find_in_sorted(tuple_0, set_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -1369
#    module_0.find_in_sorted(int_0, int_0)
