# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rpn_eval as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xa5P\x980\xb8\xdchK\x82\xd5c\x8b"
    module_0.rpn_eval(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ""
    module_0.rpn_eval(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.rpn_eval(none_type_0)


def test_case_3():
    float_0 = 2439.0701
    set_0 = {float_0, float_0, float_0, float_0}
    var_0 = module_0.rpn_eval(set_0)
    assert var_0 == pytest.approx(2439.0701, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 2439.0701
    bool_0 = True
    tuple_0 = (float_0, float_0, bool_0)
    module_0.rpn_eval(tuple_0)