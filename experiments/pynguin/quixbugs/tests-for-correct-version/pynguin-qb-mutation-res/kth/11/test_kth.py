# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kth as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    float_0 = 1528.153678815292
    module_0.kth(dict_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "CK"
    module_0.kth(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "j>3eDc9b8"
    module_0.kth(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    float_0 = 1510.378
    str_0 = "S}0 2^Oe_]iPHP,3"
    var_0 = module_0.kth(str_0, bool_0)
    assert var_0 == " "
    set_0 = {float_0, var_0, var_0, float_0}
    module_0.kth(set_0, set_0)