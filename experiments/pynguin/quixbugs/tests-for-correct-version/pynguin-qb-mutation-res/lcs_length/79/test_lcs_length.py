# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "2Iap7+q8WV||UY"
    var_0 = module_0.lcs_length(str_0, str_0)
    assert var_0 == 14
    int_0 = 1847
    none_type_0 = None
    module_0.lcs_length(none_type_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xbf\xe5\xd5\xd4a\xd0\xf9\xcf\xe1\x82"
    bytes_1 = b"\x94<\xeb\xf3\xb3\x90W\r\xd2\xfd\xaf\xb6\x06"
    var_0 = module_0.lcs_length(bytes_1, bytes_0)
    assert var_0 == 0
    str_0 = "wE2\\PH;"
    module_0.lcs_length(var_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    tuple_0 = ()
    set_0 = {tuple_0, tuple_0, tuple_0, tuple_0}
    none_type_0 = None
    module_0.lcs_length(set_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -660
    module_0.lcs_length(int_0, int_0)