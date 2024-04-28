# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rpn_eval as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"S\xfe"
    module_0.rpn_eval(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b""
    module_0.rpn_eval(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -297.5724
    dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0, float_0: float_0}
    var_0 = module_0.rpn_eval(dict_0)
    assert var_0 == pytest.approx(-297.5724, abs=0.01, rel=0.01)
    module_0.rpn_eval(var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = -1368.6
    float_1 = 581.97559
    str_0 = "{*+sb\r~?X4"
    tuple_0 = (float_0, float_1, str_0, str_0)
    module_0.rpn_eval(tuple_0)