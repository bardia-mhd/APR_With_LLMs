# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import longest_common_subsequence as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(bool_0, none_type_0)
    assert var_0 == ""
    var_1 = module_0.longest_common_subsequence(none_type_0, none_type_0)
    assert var_1 == ""
    var_2 = module_0.longest_common_subsequence(var_0, bool_0)
    assert var_2 == ""
    module_0.longest_common_subsequence(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xb8\x84\xd2M"
    module_0.longest_common_subsequence(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(none_type_0, none_type_0)
    assert var_0 == ""
    str_0 = "[+_Fcv|ro\r/,^1:@\nr"
    dict_0 = {bool_0: str_0}
    tuple_0 = (bool_0, str_0, dict_0, dict_0)
    tuple_1 = (tuple_0, dict_0, str_0, bool_0)
    module_0.longest_common_subsequence(tuple_0, tuple_1)