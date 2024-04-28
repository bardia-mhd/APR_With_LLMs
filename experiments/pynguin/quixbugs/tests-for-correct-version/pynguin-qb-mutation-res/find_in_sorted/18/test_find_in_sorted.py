# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_in_sorted as module_0
import builtins as module_1


def test_case_0():
    tuple_0 = ()
    none_type_0 = None
    var_0 = module_0.find_in_sorted(tuple_0, none_type_0)
    assert var_0 == -1
    var_1 = module_0.find_in_sorted(tuple_0, tuple_0)
    assert var_1 == -1


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ")"
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == 0
    bool_0 = False
    module_0.find_in_sorted(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    object_0 = module_1.object()
    module_0.find_in_sorted(object_0, object_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = '+,%-ogum~Rt{\x0b"lk'
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1
    bytes_0 = b"\xa8R\xcb\xe9\xbc\xafp\xbbmvWl\xe5{\x92"
    module_0.find_in_sorted(str_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "AR\t{bz"
    str_1 = 'f6>\x0c)yN,"'
    var_0 = module_0.find_in_sorted(str_1, str_1)
    assert var_0 == -1
    module_0.find_in_sorted(var_0, str_0)