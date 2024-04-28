# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rpn_eval as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x0c\xa9G\xb2\xa7e\xfd\x9e\xfdI\xea\xd6"
    module_0.rpn_eval(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    module_0.rpn_eval(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 283.8281
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.rpn_eval(list_0)
    assert var_0 == pytest.approx(283.8281, abs=0.01, rel=0.01)
    bool_0 = True
    module_0.rpn_eval(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 3166.078
    set_0 = set()
    bool_0 = True
    int_0 = 830
    dict_0 = {float_0: set_0, float_0: bool_0, int_0: float_0, float_0: bool_0}
    tuple_0 = (set_0, bool_0, set_0, dict_0)
    list_0 = [float_0, float_0, tuple_0]
    module_0.rpn_eval(list_0)