# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import lis as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    object_0 = module_0.object()
    bytes_0 = b""
    tuple_0 = (bytes_0,)
    bool_0 = False
    var_0 = module_1.lis(tuple_0)
    assert var_0 == 1
    tuple_1 = (object_0, tuple_0, bool_0)
    module_1.lis(tuple_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_1.lis(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = 'IAE;>|aq",N\ngIQ'
    var_0 = module_1.lis(str_0)
    assert var_0 == 4
    module_1.lis(var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = 'tl_\\"x}Xm?Q,m=O='
    var_0 = module_1.lis(str_0)
    assert var_0 == 4
    set_0 = set()
    var_1 = module_1.lis(set_0)
    assert var_1 == 0
    var_2 = module_1.lis(set_0)
    assert var_2 == 0
    module_1.lis(var_1)