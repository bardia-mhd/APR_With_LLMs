# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rpn_eval as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "\x0c>Z#"
    module_0.rpn_eval(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ""
    module_0.rpn_eval(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b'\xcb"\x90\xf8'
    float_0 = 205.32
    list_0 = [float_0, float_0, bytes_0, bytes_0]
    module_0.rpn_eval(list_0)