# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rpn_eval as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"r\x1d?\x86\xf16\x9f\x7f\xb8{O\x95\xef|&"
    module_0.rpn_eval(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b""
    module_0.rpn_eval(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -644.191597
    dict_0 = {float_0: float_0}
    tuple_0 = (dict_0,)
    tuple_1 = (float_0, tuple_0)
    module_0.rpn_eval(tuple_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = -246.474001
    tuple_0 = (float_0, float_0)
    bool_0 = True
    tuple_1 = (tuple_0, bool_0)
    str_0 = "tSB/_e"
    tuple_2 = (float_0, float_0, tuple_1, str_0)
    module_0.rpn_eval(tuple_2)