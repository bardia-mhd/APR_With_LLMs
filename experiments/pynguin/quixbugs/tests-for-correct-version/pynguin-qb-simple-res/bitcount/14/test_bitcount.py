# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bitcount as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -463
    module_0.bitcount(int_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.bitcount(none_type_0)
    assert var_0 == 0


def test_case_2():
    list_0 = []
    var_0 = module_0.bitcount(list_0)
    assert var_0 == 0
    bool_0 = True
    var_1 = module_0.bitcount(bool_0)
    assert var_1 == 1
    var_2 = module_0.bitcount(var_1)
    assert var_2 == 1