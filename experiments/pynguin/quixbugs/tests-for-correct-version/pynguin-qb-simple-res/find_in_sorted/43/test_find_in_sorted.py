# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_in_sorted as module_0


def test_case_0():
    list_0 = []
    none_type_0 = None
    var_0 = module_0.find_in_sorted(list_0, none_type_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    set_0 = {bool_0, bool_0}
    none_type_0 = None
    module_0.find_in_sorted(set_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = '8x_m:!):"4#:yk@f!'
    tuple_0 = ()
    set_0 = {str_0, tuple_0, str_0, str_0}
    tuple_1 = (set_0,)
    var_0 = module_0.find_in_sorted(tuple_1, set_0)
    assert var_0 == 0
    str_1 = "XZ&Ty?SA)<AAlcTy"
    none_type_0 = None
    var_1 = module_0.find_in_sorted(str_1, str_1)
    assert var_1 == -1
    module_0.find_in_sorted(str_1, none_type_0)