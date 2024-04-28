# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rpn_eval as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xcd\\'\x8a\x9cY\x84R\xde\x89\x7f\xab\x85\xa91\xe5\xc8\xf3V9"
    module_0.rpn_eval(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    module_0.rpn_eval(set_0)


def test_case_2():
    float_0 = 416.67
    list_0 = [float_0]
    var_0 = module_0.rpn_eval(list_0)
    assert var_0 == pytest.approx(416.67, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 168.01105861721297
    bool_0 = True
    tuple_0 = (float_0, float_0, bool_0)
    module_0.rpn_eval(tuple_0)