# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import longest_common_subsequence as module_1


def test_case_0():
    object_0 = module_0.object()
    none_type_0 = None
    var_0 = module_1.longest_common_subsequence(object_0, none_type_0)
    assert var_0 == ""


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    var_0 = module_1.longest_common_subsequence(bool_0, bool_0)
    assert var_0 == ""
    bool_1 = True
    list_0 = [bool_1, bool_1]
    module_1.longest_common_subsequence(bool_1, list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    object_0 = module_0.object()
    module_1.longest_common_subsequence(object_0, object_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Fvc*5\\M=-_p^biJ\x0cPCT"
    var_0 = module_1.longest_common_subsequence(str_0, str_0)
    assert var_0 == "Fvc*5\\M=-_p^biJ\x0cPCT"
    dict_0 = {str_0: str_0}
    bool_0 = False
    var_1 = module_1.longest_common_subsequence(dict_0, bool_0)
    assert var_1 == ""
    list_0 = [dict_0, dict_0, str_0, dict_0]
    module_1.longest_common_subsequence(list_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    tuple_0 = (bool_0,)
    list_0 = [tuple_0, tuple_0, bool_0]
    list_1 = [list_0, tuple_0, list_0, list_0]
    module_1.longest_common_subsequence(list_1, list_0)