# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bitcount as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -4522
    list_0 = [int_0]
    module_0.bitcount(list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    var_0 = module_0.bitcount(none_type_0)
    assert var_0 == 0
    str_0 = 's.";#0,z'
    module_0.bitcount(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -1367
    module_0.bitcount(int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    var_0 = module_0.bitcount(bool_0)
    assert var_0 == 1
    var_1 = module_0.bitcount(var_0)
    assert var_1 == 1
    var_2 = module_0.bitcount(var_0)
    assert var_2 == 1
    str_0 = "p\tdcy<ij,(c:"
    var_3 = module_0.bitcount(var_0)
    assert var_3 == 1
    var_4 = module_0.bitcount(var_0)
    assert var_4 == 1
    var_5 = module_0.bitcount(var_1)
    assert var_5 == 1
    var_6 = module_0.bitcount(var_3)
    assert var_6 == 1
    var_7 = module_0.bitcount(var_4)
    assert var_7 == 1
    module_0.bitcount(str_0)