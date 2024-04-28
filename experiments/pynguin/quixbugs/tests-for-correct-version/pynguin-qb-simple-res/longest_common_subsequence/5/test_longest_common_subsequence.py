# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import longest_common_subsequence as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"[\xef\xf4\xf0\x92\xa69O|\xfa\xdf\x8cs\x19"
    module_0.longest_common_subsequence(bytes_0, bytes_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(none_type_0, none_type_0)
    assert var_0 == ""
    none_type_1 = None
    var_1 = module_0.longest_common_subsequence(none_type_1, none_type_1)
    assert var_1 == ""
    var_2 = module_0.longest_common_subsequence(var_1, var_1)
    assert var_2 == ""
    var_3 = module_0.longest_common_subsequence(var_1, var_1)
    assert var_3 == ""
    list_0 = [var_1, var_1]
    var_4 = module_0.longest_common_subsequence(none_type_0, var_2)
    assert var_4 == ""
    var_5 = module_0.longest_common_subsequence(var_3, var_1)
    assert var_5 == ""
    var_6 = module_0.longest_common_subsequence(list_0, var_1)
    assert var_6 == ""
    var_7 = module_0.longest_common_subsequence(list_0, var_1)
    assert var_7 == ""
    var_8 = module_0.longest_common_subsequence(var_6, var_3)
    assert var_8 == ""


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "\\ADs:#> w1|"
    list_0 = [str_0, str_0]
    var_0 = module_0.longest_common_subsequence(str_0, str_0)
    assert var_0 == "\\ADs:#> w1|"
    var_1 = module_0.longest_common_subsequence(list_0, str_0)
    assert var_1 == ""
    var_2 = module_0.longest_common_subsequence(list_0, list_0)
    assert var_2 == "\\ADs:#> w1|\\ADs:#> w1|"
    bool_0 = True
    float_0 = 426.71119
    var_3 = module_0.longest_common_subsequence(var_1, float_0)
    assert var_3 == ""
    module_0.longest_common_subsequence(bool_0, bool_0)