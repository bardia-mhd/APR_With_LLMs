# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import wrap as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    module_0.wrap(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = 874.0
    set_0 = {float_0, float_0}
    var_0 = module_0.wrap(set_0, float_0)
    none_type_0 = None
    module_0.wrap(none_type_0, none_type_0)


def test_case_2():
    bool_0 = True
    str_0 = "O>yM1A;Y~S_Y3a"
    var_0 = module_0.wrap(str_0, bool_0)