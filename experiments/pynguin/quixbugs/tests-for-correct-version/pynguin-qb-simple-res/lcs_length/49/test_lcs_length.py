# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import lcs_length as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    object_0 = module_0.object()
    str_0 = "8tGqw{X[r~xK#P/D,\\8k"
    bool_0 = False
    tuple_0 = (object_0, str_0, bool_0)
    var_0 = module_1.lcs_length(tuple_0, tuple_0)
    assert var_0 == 3
    bool_1 = True
    module_1.lcs_length(bool_1, bool_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x80\x1a_*b\xbf\xd0\xf2\xc5A\xcd\xd4\x10\xff]\xf7{,"
    tuple_0 = (bytes_0,)
    var_0 = module_1.lcs_length(tuple_0, bytes_0)
    assert var_0 == 0
    module_1.lcs_length(var_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_1.lcs_length(none_type_0, none_type_0)