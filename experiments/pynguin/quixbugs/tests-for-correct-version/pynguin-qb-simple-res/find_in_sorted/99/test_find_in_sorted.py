# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_in_sorted as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    set_0 = set()
    none_type_0 = None
    var_0 = module_0.find_in_sorted(set_0, none_type_0)
    assert var_0 == -1
    module_0.find_in_sorted(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xcbi\r\x9d5\x19#\x17\xdd\xa4\x11M"
    module_0.find_in_sorted(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    bytes_0 = b"\xcb\x18\xe1\xc2\xf9\xc2\xc3\x00\xed"
    module_0.find_in_sorted(bool_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "%FR)}&+F>-C)oZ"
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1
    var_1 = module_0.find_in_sorted(str_0, str_0)
    assert var_1 == -1
    none_type_0 = None
    var_2 = module_0.find_in_sorted(str_0, str_0)
    assert var_2 == -1
    module_0.find_in_sorted(str_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "R6"
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1
    float_0 = 1947.663425
    module_0.find_in_sorted(float_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\xafkO\xce\xcf\x7f\xfe\xecc\xdb\x10\xc9"
    tuple_0 = (bytes_0,)
    var_0 = module_0.find_in_sorted(tuple_0, bytes_0)
    assert var_0 == 0
    module_0.find_in_sorted(tuple_0, var_0)