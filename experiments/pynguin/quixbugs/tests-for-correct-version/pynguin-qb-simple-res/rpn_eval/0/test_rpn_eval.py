# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rpn_eval as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xb0\x08c\x8dV\xae\xea\r\xd6\xa7[\xcfNG\xb0"
    module_0.rpn_eval(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    module_0.rpn_eval(list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 104
    module_0.rpn_eval(int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -1
    float_0 = -2166.2671
    set_0 = {int_0, float_0}
    module_0.rpn_eval(set_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 965.0
    dict_0 = {}
    object_0 = module_1.object(**dict_0)
    bool_0 = True
    tuple_0 = (object_0, bool_0)
    tuple_1 = (float_0, float_0, tuple_0, dict_0)
    module_0.rpn_eval(tuple_1)