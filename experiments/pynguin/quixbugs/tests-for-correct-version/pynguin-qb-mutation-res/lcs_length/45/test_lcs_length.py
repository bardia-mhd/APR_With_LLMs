# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\\\x80U}\xee\xc9\xa8\xa1\x87+\x94"
    var_0 = module_0.lcs_length(bytes_0, bytes_0)
    assert var_0 == 11
    none_type_0 = None
    module_0.lcs_length(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    var_0 = module_0.lcs_length(tuple_0, tuple_0)
    assert var_0 == 0
    set_0 = {tuple_0, tuple_0}
    var_1 = module_0.lcs_length(set_0, tuple_0)
    assert var_1 == 0
    module_0.lcs_length(var_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.lcs_length(none_type_0, none_type_0)