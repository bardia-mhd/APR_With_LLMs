# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bitcount as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "X\\sZ"
    module_0.bitcount(str_0)


def test_case_1():
    bool_0 = False
    var_0 = module_0.bitcount(bool_0)
    assert var_0 == 0


def test_case_2():
    int_0 = 1119
    var_0 = module_0.bitcount(int_0)
    assert var_0 == 7
    var_1 = module_0.bitcount(var_0)
    assert var_1 == 3
    var_2 = module_0.bitcount(int_0)
    assert var_2 == 7
    bool_0 = False
    var_3 = module_0.bitcount(bool_0)
    assert var_3 == 0