# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_in_sorted as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    dict_0 = {}
    var_0 = module_0.find_in_sorted(dict_0, dict_0)
    assert var_0 == -1
    int_0 = 1874
    module_0.find_in_sorted(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xb6CZ\x81D\xc8\x83\xc7\xbc8\xeb\xefYo\xe8\x18>\xa3\x1d\x88"
    list_0 = [bytes_0, bytes_0, bytes_0]
    none_type_0 = None
    module_0.find_in_sorted(list_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    none_type_0 = None
    module_0.find_in_sorted(bool_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = 'R"0?TE6\n(!Gx'
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1
    module_0.find_in_sorted(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "MA"
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1
    float_0 = 445.6
    module_0.find_in_sorted(float_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.find_in_sorted(list_0, bool_0)
    assert var_0 == 1
    int_0 = 241
    module_0.find_in_sorted(int_0, int_0)