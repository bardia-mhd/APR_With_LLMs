# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import bitcount as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    object_0 = module_0.object()
    module_1.bitcount(object_0)


def test_case_1():
    tuple_0 = ()
    var_0 = module_1.bitcount(tuple_0)
    assert var_0 == 0
    var_1 = module_1.bitcount(var_0)
    assert var_1 == 0
    var_2 = module_1.bitcount(tuple_0)
    assert var_2 == 0
    var_3 = module_1.bitcount(var_1)
    assert var_3 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 714
    var_0 = module_1.bitcount(int_0)
    assert var_0 == 5
    bool_0 = True
    set_0 = {bool_0}
    module_1.bitcount(set_0)