# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import longest_common_subsequence as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 709
    module_0.longest_common_subsequence(int_0, int_0)


def test_case_1():
    int_0 = -5402
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(none_type_0, none_type_0)
    assert var_0 == ""
    list_0 = [none_type_0, var_0, int_0, var_0]
    var_1 = module_0.longest_common_subsequence(list_0, none_type_0)
    assert var_1 == ""
    var_2 = module_0.longest_common_subsequence(int_0, none_type_0)
    assert var_2 == ""


def test_case_2():
    str_0 = ""
    tuple_0 = (str_0,)
    list_0 = [str_0, str_0]
    var_0 = module_0.longest_common_subsequence(tuple_0, list_0)
    assert var_0 == ""
    none_type_0 = None
    var_1 = module_0.longest_common_subsequence(none_type_0, none_type_0)
    assert var_1 == ""


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ""
    tuple_0 = (str_0,)
    list_0 = [str_0, str_0]
    var_0 = module_0.longest_common_subsequence(tuple_0, list_0)
    assert var_0 == ""
    var_1 = module_0.longest_common_subsequence(var_0, tuple_0)
    assert var_1 == ""
    var_2 = module_0.longest_common_subsequence(str_0, list_0)
    assert var_2 == ""
    str_1 = "}?*'gCI#{n\tYX"
    var_3 = module_0.longest_common_subsequence(tuple_0, str_1)
    assert var_3 == ""
    module_1.object(*list_0, **list_0)