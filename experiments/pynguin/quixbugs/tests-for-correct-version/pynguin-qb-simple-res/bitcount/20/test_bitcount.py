# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bitcount as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "h\\#:u-u=-?vMT"
    module_0.bitcount(str_0)


def test_case_1():
    dict_0 = {}
    none_type_0 = None
    var_0 = module_0.bitcount(none_type_0)
    assert var_0 == 0
    var_1 = module_0.bitcount(dict_0)
    assert var_1 == 0
    var_2 = module_0.bitcount(var_0)
    assert var_2 == 0
    var_3 = module_0.bitcount(var_0)
    assert var_3 == 0
    var_4 = module_0.bitcount(var_1)
    assert var_4 == 0
    var_5 = module_0.bitcount(var_1)
    assert var_5 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 1584
    var_0 = module_0.bitcount(int_0)
    assert var_0 == 4
    none_type_0 = None
    var_1 = module_0.bitcount(none_type_0)
    assert var_1 == 0
    var_2 = module_0.bitcount(var_1)
    assert var_2 == 0
    var_3 = module_0.bitcount(var_1)
    assert var_3 == 0
    var_4 = module_0.bitcount(var_2)
    assert var_4 == 0
    var_5 = module_0.bitcount(none_type_0)
    assert var_5 == 0
    bytes_0 = b"\x00y\xcf\xd3\xe38"
    module_0.bitcount(bytes_0)


def test_case_3():
    bool_0 = True
    var_0 = module_0.bitcount(bool_0)
    assert var_0 == 1