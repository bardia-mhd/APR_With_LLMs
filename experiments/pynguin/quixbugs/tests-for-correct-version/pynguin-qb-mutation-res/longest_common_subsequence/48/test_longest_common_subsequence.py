# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import longest_common_subsequence as module_0


def test_case_0():
    str_0 = "B$u!@*ih! {k',w"
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(str_0, none_type_0)
    assert var_0 == ""


def test_case_1():
    bool_0 = False
    var_0 = module_0.longest_common_subsequence(bool_0, bool_0)
    assert var_0 == ""
    var_1 = module_0.longest_common_subsequence(var_0, var_0)
    assert var_1 == ""


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(none_type_0, bool_0)
    assert var_0 == ""
    module_0.longest_common_subsequence(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    int_0 = 153
    str_0 = "BzG><A,TZs=u\r6"
    bytes_0 = b"\xf7\x0f"
    var_0 = module_0.longest_common_subsequence(bool_0, int_0)
    assert var_0 == ""
    var_1 = module_0.longest_common_subsequence(str_0, bool_0)
    assert var_1 == ""
    module_0.longest_common_subsequence(bytes_0, bytes_0)


def test_case_4():
    str_0 = "n?a@>ur"
    list_0 = [str_0]
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(list_0, str_0)
    assert var_0 == ""
    var_1 = module_0.longest_common_subsequence(list_0, none_type_0)
    assert var_1 == ""