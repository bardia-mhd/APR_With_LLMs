# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0
import builtins as module_1


def test_case_0():
    int_0 = -965
    bool_0 = False
    tuple_0 = (int_0, bool_0)
    list_0 = [tuple_0, bool_0, bool_0]
    var_0 = module_0.lcs_length(list_0, list_0)
    assert var_0 == 3


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xec.\xbff\xa9\x98\x95\xac\xce"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.lcs_length(list_0, bytes_0)
    assert var_0 == 0
    object_0 = module_1.object()
    module_0.lcs_length(object_0, object_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    complex_0 = 2697.05 - 1655.0924j
    module_0.lcs_length(complex_0, complex_0)