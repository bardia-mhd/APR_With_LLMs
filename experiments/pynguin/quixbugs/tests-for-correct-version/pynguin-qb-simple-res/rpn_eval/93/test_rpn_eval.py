# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rpn_eval as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xe9\x0b\xb5\xd0K\x14\xf5P\x8a"
    module_0.rpn_eval(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    module_0.rpn_eval(list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 92.025
    module_0.rpn_eval(float_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 1368.7614
    int_0 = 986
    list_0 = [float_0, float_0, int_0]
    module_0.rpn_eval(list_0)