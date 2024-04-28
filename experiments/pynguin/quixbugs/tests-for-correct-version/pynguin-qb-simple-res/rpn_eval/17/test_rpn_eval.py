# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rpn_eval as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "Cx%l EG;"
    module_0.rpn_eval(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ""
    module_0.rpn_eval(str_0)


def test_case_2():
    float_0 = -633.8
    set_0 = {float_0}
    var_0 = module_0.rpn_eval(set_0)
    assert var_0 == pytest.approx(-633.8, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 4817.715
    float_1 = -82.31716
    bool_0 = True
    tuple_0 = (float_0, float_1, bool_0)
    module_0.rpn_eval(tuple_0)