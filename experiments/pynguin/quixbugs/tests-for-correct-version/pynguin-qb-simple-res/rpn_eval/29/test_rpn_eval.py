# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rpn_eval as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b'\xd7\x9fm\x18\xbc\x16\x15\x82"\xad}\x08^\xa0\xe9'
    module_0.rpn_eval(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    module_0.rpn_eval(set_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.rpn_eval(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = -1733.376
    complex_0 = -2405 + 4766.865821j
    list_0 = [float_0, float_0, float_0, complex_0]
    module_0.rpn_eval(list_0)