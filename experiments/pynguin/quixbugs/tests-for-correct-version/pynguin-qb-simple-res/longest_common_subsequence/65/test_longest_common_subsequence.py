# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import longest_common_subsequence as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 509
    set_0 = {int_0, int_0}
    module_0.longest_common_subsequence(set_0, int_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(none_type_0, none_type_0)
    assert var_0 == ""


def test_case_2():
    bytes_0 = b'\xc0\xcfK*\xe3GY\xbajr\x19"\x1eF\xccT\x89\xa1'
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.longest_common_subsequence(bytes_0, list_0)
    assert var_0 == ""
    var_1 = module_0.longest_common_subsequence(var_0, var_0)
    assert var_1 == ""


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x7f\xd3\x0e\xa6!\x10>\xcb\xe9\x9cW\x06\x94\xf3"
    module_0.longest_common_subsequence(bytes_0, bytes_0)