# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import longest_common_subsequence as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 2340
    module_0.longest_common_subsequence(int_0, int_0)


def test_case_1():
    str_0 = "P=p-\tZz"
    var_0 = module_0.longest_common_subsequence(str_0, str_0)
    assert var_0 == "P=p-\tZz"


def test_case_2():
    list_0 = []
    object_0 = module_1.object(*list_0)
    var_0 = module_0.longest_common_subsequence(object_0, list_0)
    assert var_0 == ""


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Kv+?0 =P"
    tuple_0 = (str_0,)
    var_0 = module_0.longest_common_subsequence(tuple_0, tuple_0)
    assert var_0 == "Kv+?0 =P"
    var_1 = module_0.longest_common_subsequence(tuple_0, str_0)
    assert var_1 == ""
    object_0 = module_1.object()
    module_0.longest_common_subsequence(object_0, object_0)