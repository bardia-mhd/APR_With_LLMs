# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import longest_common_subsequence as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x9f\xb2\x96\x84\x96\xdc\x93\xcc\x0e\x17L6\xcdk\x9d}]"
    list_0 = [bytes_0, bytes_0]
    module_0.longest_common_subsequence(list_0, list_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(none_type_0, none_type_0)
    assert var_0 == ""


def test_case_2():
    bytes_0 = b""
    set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
    var_0 = module_0.longest_common_subsequence(set_0, bytes_0)
    assert var_0 == ""
    var_1 = module_0.longest_common_subsequence(var_0, var_0)
    assert var_1 == ""


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "p>l~eL)0\x0b"
    list_0 = [str_0, str_0]
    var_0 = module_0.longest_common_subsequence(str_0, list_0)
    assert var_0 == ""
    var_1 = module_0.longest_common_subsequence(list_0, list_0)
    assert var_1 == "p>l~eL)0\x0bp>l~eL)0\x0b"
    var_2 = module_0.longest_common_subsequence(list_0, list_0)
    assert var_2 == "p>l~eL)0\x0bp>l~eL)0\x0b"
    int_0 = 1131
    var_3 = module_0.longest_common_subsequence(var_1, var_0)
    assert var_3 == ""
    module_0.longest_common_subsequence(int_0, int_0)