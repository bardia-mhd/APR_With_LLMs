# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0


def test_case_0():
    bytes_0 = b"\xd4_Bx/*a\xfa"
    var_0 = module_0.lcs_length(bytes_0, bytes_0)
    assert var_0 == 8


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    var_0 = module_0.lcs_length(set_0, set_0)
    assert var_0 == 0
    none_type_0 = None
    bool_0 = False
    module_0.lcs_length(none_type_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -702
    module_0.lcs_length(int_0, int_0)