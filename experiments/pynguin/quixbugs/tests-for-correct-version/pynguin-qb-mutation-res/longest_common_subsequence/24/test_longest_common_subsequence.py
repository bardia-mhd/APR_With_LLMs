# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import longest_common_subsequence as module_1


def test_case_0():
    list_0 = []
    object_0 = module_0.object(*list_0)
    none_type_0 = None
    var_0 = module_1.longest_common_subsequence(object_0, none_type_0)
    assert var_0 == ""


def test_case_1():
    list_0 = []
    var_0 = module_1.longest_common_subsequence(list_0, list_0)
    assert var_0 == ""


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -3377
    set_0 = {int_0, int_0, int_0}
    module_1.longest_common_subsequence(set_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xd9\xff*\x18{f\x9e:"
    module_1.longest_common_subsequence(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    int_0 = -2421
    tuple_0 = (dict_0, int_0)
    list_0 = [tuple_0, bool_0, tuple_0, tuple_0]
    list_1 = [list_0, list_0]
    module_1.longest_common_subsequence(list_1, dict_0)