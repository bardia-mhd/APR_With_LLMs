# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rpn_eval as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "2-\"(Bk{NU\x0bY'(O("
    module_0.rpn_eval(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    module_0.rpn_eval(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.rpn_eval(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = -3468.8494
    object_0 = module_1.object()
    dict_0 = {float_0: float_0, float_0: float_0, object_0: object_0}
    module_0.rpn_eval(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 94.7878
    tuple_0 = ()
    tuple_1 = (float_0, float_0, tuple_0, float_0)
    module_0.rpn_eval(tuple_1)