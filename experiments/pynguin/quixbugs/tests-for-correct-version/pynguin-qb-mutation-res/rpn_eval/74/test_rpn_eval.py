# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rpn_eval as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x0e)L\x16\xfa\x0f"
    module_0.rpn_eval(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b""
    module_0.rpn_eval(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.rpn_eval(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 17.335477
    bool_0 = False
    tuple_0 = (float_0, float_0, bool_0)
    module_0.rpn_eval(tuple_0)