# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0


def test_case_0():
    bool_0 = False
    var_0 = module_0.possible_change(bool_0, bool_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    module_0.possible_change(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -2240.008
    var_0 = module_0.possible_change(float_0, float_0)
    assert var_0 == 0
    var_1 = module_0.possible_change(float_0, float_0)
    assert var_1 == 0
    bytes_0 = b"\xa3M."
    str_0 = "kmi.lb"
    module_0.possible_change(bytes_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    none_type_0 = None
    var_0 = module_0.possible_change(none_type_0, bool_0)
    assert var_0 == 0
    module_0.possible_change(bool_0, bool_0)