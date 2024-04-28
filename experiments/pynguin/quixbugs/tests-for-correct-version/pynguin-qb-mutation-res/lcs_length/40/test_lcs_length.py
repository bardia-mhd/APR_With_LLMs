# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "nc\\f8IIl+mtm\rLTms+ST"
    var_0 = module_0.lcs_length(str_0, str_0)
    assert var_0 == 20
    module_0.lcs_length(str_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    var_0 = module_0.lcs_length(dict_0, dict_0)
    assert var_0 == 0
    list_0 = [dict_0, dict_0]
    var_1 = module_0.lcs_length(list_0, dict_0)
    assert var_1 == 0
    float_0 = -3677.309
    module_0.lcs_length(float_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 1316.303
    set_0 = {float_0, float_0}
    module_0.lcs_length(set_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    dict_0 = {}
    module_0.lcs_length(none_type_0, dict_0)