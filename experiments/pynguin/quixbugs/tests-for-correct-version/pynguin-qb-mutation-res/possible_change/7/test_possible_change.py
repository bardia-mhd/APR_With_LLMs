# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    var_0 = module_0.possible_change(bool_0, bool_0)
    assert var_0 == 1
    int_0 = -150
    module_0.possible_change(int_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.possible_change(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xba%gyn)\x9d\xdf\x94\x83\xd4U\xf7Tn6\xc8&\xea\x87"
    float_0 = -491.7608
    var_0 = module_0.possible_change(bytes_0, float_0)
    assert var_0 == 0
    list_0 = []
    module_0.possible_change(var_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 1781.37
    module_0.possible_change(float_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    int_0 = 184
    none_type_0 = None
    var_0 = module_0.possible_change(none_type_0, bool_0)
    assert var_0 == 0
    module_0.possible_change(int_0, none_type_0)