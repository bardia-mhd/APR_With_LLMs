# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rpn_eval as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "DHSt\nNT_AM,?b\x0c"
    module_0.rpn_eval(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    module_0.rpn_eval(set_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 1759
    module_0.rpn_eval(int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 2424.33241
    int_0 = 3248
    tuple_0 = (float_0, float_0, float_0, int_0)
    module_0.rpn_eval(tuple_0)