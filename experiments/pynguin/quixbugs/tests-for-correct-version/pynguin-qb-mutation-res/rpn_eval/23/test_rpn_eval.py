# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rpn_eval as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"[\xaeYp\xcb\x11\x8a>\x94(\xe9o,\xdf\xbcH\x08"
    module_0.rpn_eval(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b""
    module_0.rpn_eval(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -367.82
    bool_0 = False
    tuple_0 = (float_0, float_0, bool_0, bool_0)
    module_0.rpn_eval(tuple_0)