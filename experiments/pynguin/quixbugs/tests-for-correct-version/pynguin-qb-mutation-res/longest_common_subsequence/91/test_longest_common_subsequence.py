# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import longest_common_subsequence as module_0


def test_case_0():
    int_0 = -614
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(int_0, none_type_0)
    assert var_0 == ""


def test_case_1():
    bool_0 = False
    var_0 = module_0.longest_common_subsequence(bool_0, bool_0)
    assert var_0 == ""
    list_0 = [bool_0, bool_0, bool_0]
    var_1 = module_0.longest_common_subsequence(list_0, bool_0)
    assert var_1 == ""


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 1105
    module_0.longest_common_subsequence(int_0, int_0)


def test_case_3():
    str_0 = "{\tS/Zch"
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(str_0, str_0)
    assert var_0 == "{\tS/Zch"
    var_1 = module_0.longest_common_subsequence(none_type_0, none_type_0)
    assert var_1 == ""
    set_0 = {str_0, var_1}
    var_2 = module_0.longest_common_subsequence(var_1, set_0)
    assert var_2 == ""
    var_3 = module_0.longest_common_subsequence(set_0, var_1)
    assert var_3 == ""
    tuple_0 = (set_0, var_1, var_1)
    var_4 = module_0.longest_common_subsequence(tuple_0, str_0)
    assert var_4 == ""
    var_5 = module_0.longest_common_subsequence(none_type_0, str_0)
    var_6 = module_0.longest_common_subsequence(str_0, none_type_0)


def test_case_4():
    bool_0 = True
    bytes_0 = b"\x18T\x16\x1b}o^\xd7\xa6\xe3\xb4"
    set_0 = {bool_0, bool_0, bool_0, bytes_0}
    list_0 = [set_0, bool_0, bool_0, bytes_0]
    var_0 = module_0.longest_common_subsequence(list_0, bytes_0)
    assert var_0 == ""