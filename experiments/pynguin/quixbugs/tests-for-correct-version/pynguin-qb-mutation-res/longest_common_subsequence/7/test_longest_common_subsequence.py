# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import longest_common_subsequence as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -715.900572
    module_0.longest_common_subsequence(float_0, float_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(none_type_0, none_type_0)
    assert var_0 == ""


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -1764
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(none_type_0, int_0)
    assert var_0 == ""
    var_1 = module_0.longest_common_subsequence(int_0, none_type_0)
    assert var_1 == ""
    var_2 = module_0.longest_common_subsequence(var_1, none_type_0)
    assert var_2 == ""
    module_0.longest_common_subsequence(int_0, int_0)


def test_case_3():
    str_0 = "'Q#"
    var_0 = module_0.longest_common_subsequence(str_0, str_0)
    assert var_0 == "'Q#"
    dict_0 = {}
    var_1 = module_0.longest_common_subsequence(dict_0, dict_0)
    assert var_1 == ""


def test_case_4():
    bool_0 = False
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(bool_0, none_type_0)
    assert var_0 == ""
    bytes_0 = b"\xde\xe8\xbc^\xa3\x82\xf0\xf8\x0e\x9e\xea\xdb\x1a\xf1"
    list_0 = [var_0, bool_0, bool_0, bool_0]
    var_1 = module_0.longest_common_subsequence(list_0, none_type_0)
    assert var_1 == ""
    var_2 = module_0.longest_common_subsequence(bytes_0, list_0)
    assert var_2 == ""
    var_3 = module_0.longest_common_subsequence(var_0, var_0)
    assert var_3 == ""
    var_4 = module_0.longest_common_subsequence(none_type_0, none_type_0)
    assert var_4 == ""
    var_5 = module_0.longest_common_subsequence(bytes_0, var_2)
    assert var_5 == ""
    var_6 = module_0.longest_common_subsequence(var_5, bool_0)
    assert var_6 == ""