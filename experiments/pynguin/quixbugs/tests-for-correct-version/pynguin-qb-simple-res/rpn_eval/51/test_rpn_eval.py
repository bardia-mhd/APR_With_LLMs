# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rpn_eval as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x1c\xa1\xda\xba\x15_"
    module_0.rpn_eval(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    module_0.rpn_eval(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.rpn_eval(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 2606.814902
    dict_0 = {}
    tuple_0 = (float_0, float_0, dict_0)
    module_0.rpn_eval(tuple_0)