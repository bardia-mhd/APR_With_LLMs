# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rpn_eval as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "vBqr.}X:s&M^bk"
    module_0.rpn_eval(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ""
    module_0.rpn_eval(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    object_0 = module_1.object()
    module_0.rpn_eval(object_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = -46.8852
    bool_0 = False
    bool_1 = True
    tuple_0 = (float_0, float_0, bool_0, bool_1)
    module_0.rpn_eval(tuple_0)