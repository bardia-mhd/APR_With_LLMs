# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "CPd:"
    var_0 = module_0.lcs_length(str_0, str_0)
    assert var_0 == 4
    var_1 = module_0.lcs_length(str_0, str_0)
    assert var_1 == 4
    module_0.lcs_length(str_0, var_1)


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.lcs_length(tuple_0, tuple_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -1663
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0, int_0: int_0}
    none_type_0 = None
    module_0.lcs_length(dict_0, none_type_0)