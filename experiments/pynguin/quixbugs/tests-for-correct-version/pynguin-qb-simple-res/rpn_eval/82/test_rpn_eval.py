# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rpn_eval as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "iHK7cLQl\x0bz"
    module_0.rpn_eval(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    module_0.rpn_eval(set_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.rpn_eval(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 1083.0
    list_0 = [float_0]
    var_0 = module_0.rpn_eval(list_0)
    assert var_0 == pytest.approx(1083.0, abs=0.01, rel=0.01)
    module_0.rpn_eval(float_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = -4051.322639
    list_0 = [float_0, float_0, float_0, float_0]
    list_1 = [float_0, float_0, list_0, list_0]
    module_0.rpn_eval(list_1)