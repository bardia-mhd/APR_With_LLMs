# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import wrap as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -2873.0181
    dict_0 = {float_0: float_0, float_0: float_0}
    module_0.wrap(dict_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "p`\tq"
    module_0.wrap(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    set_0 = {bool_0, bool_0, bool_0}
    var_0 = module_0.wrap(set_0, bool_0)
    int_0 = -545
    module_0.wrap(var_0, int_0)


def test_case_3():
    bool_0 = True
    str_0 = "F9RuYCy\t0(TmO&Y3<e!"
    var_0 = module_0.wrap(str_0, bool_0)