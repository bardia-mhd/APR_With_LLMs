# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0


def test_case_0():
    bytes_0 = b"\x9b"
    var_0 = module_0.lcs_length(bytes_0, bytes_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    var_0 = module_0.lcs_length(set_0, set_0)
    assert var_0 == 0
    var_1 = module_0.lcs_length(set_0, set_0)
    assert var_1 == 0
    module_0.lcs_length(var_1, var_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.lcs_length(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xa8\xddFJ\xe4\xa2\x84\xb6v\xe4\x01\xd3X"
    var_0 = module_0.lcs_length(bytes_0, bytes_0)
    assert var_0 == 13
    module_0.lcs_length(var_0, var_0)