# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_first_in_sorted as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "KFw1Xd\x0b0sBTLQ*]OF1O"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1
    none_type_0 = None
    module_0.find_first_in_sorted(none_type_0, none_type_0)


def test_case_1():
    dict_0 = {}
    var_0 = module_0.find_first_in_sorted(dict_0, dict_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.find_first_in_sorted(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = 'FP^%4r$\x0b"fD3w}m'
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1
    none_type_0 = None
    bytes_0 = b"\xc4:"
    none_type_1 = None
    list_0 = [bytes_0, none_type_1, none_type_1, none_type_0]
    module_0.find_first_in_sorted(list_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "*<"
    bytes_0 = b'\x1f\x02\x03\xe6\x99U\xb2\xe0\xdfi\xf1e\xd1"'
    set_0 = {str_0, bytes_0}
    int_0 = 2806
    tuple_0 = (str_0, set_0, int_0)
    var_0 = module_0.find_first_in_sorted(tuple_0, set_0)
    assert var_0 == 1
    int_1 = -210
    module_0.find_first_in_sorted(int_1, set_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "j"
    bytes_0 = b'\x1f\x02\x03\xe6\x99U\xb2\xe0\xdfi\xf1e\xd1"'
    set_0 = {str_0, bytes_0}
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == 0
    int_0 = 2004
    tuple_0 = (str_0, set_0, int_0)
    var_1 = module_0.find_first_in_sorted(tuple_0, set_0)
    assert var_1 == 1
    int_1 = -210
    module_0.find_first_in_sorted(int_1, set_0)