# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1778 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    int_0 = -4377
    set_0 = {int_0, int_0}
    tuple_0 = (int_0, set_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == -4378


def test_case_2():
    int_0 = 220
    str_0 = "BB!V8^!0f2"
    list_0 = [int_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 211


def test_case_3():
    int_0 = 1476
    str_0 = "BB!VaRR8^D\tf"
    list_0 = [int_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1466


def test_case_4():
    int_0 = 1476
    str_0 = "BB!VaRR8[GGm^D\tf"
    list_0 = [int_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1463


def test_case_5():
    int_0 = 1436
    str_0 = "BB!VaRRR8*GGm^D\ty"
    list_0 = [int_0, str_0, str_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1423


def test_case_6():
    int_0 = -2523
    str_0 = "BB!aRRR8*GGG^D[gy"
    list_0 = [int_0, str_0, str_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -2535


def test_case_7():
    int_0 = -1779
    str_0 = "BBBaRRR8+*GGG^D[gy"
    list_0 = [int_0, str_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -1791