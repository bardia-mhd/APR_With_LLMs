# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bitcount as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "(W]t?%,8'j<("
    module_0.bitcount(str_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.bitcount(none_type_0)
    assert var_0 == 0
    var_1 = module_0.bitcount(none_type_0)
    assert var_1 == 0
    var_2 = module_0.bitcount(var_0)
    assert var_2 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -1744
    module_0.bitcount(int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    var_0 = module_0.bitcount(bool_0)
    assert var_0 == 1
    var_1 = module_0.bitcount(var_0)
    assert var_1 == 1
    bytes_0 = b"W\xf033?{"
    none_type_0 = None
    var_2 = module_0.bitcount(var_1)
    assert var_2 == 1
    var_3 = module_0.bitcount(var_0)
    assert var_3 == 1
    var_4 = module_0.bitcount(none_type_0)
    assert var_4 == 0
    module_0.bitcount(bytes_0)