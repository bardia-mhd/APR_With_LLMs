# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1929 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"PJm\xaeV\xe8\x1dO\x0e\xbf_m\x983\x12n\xfc\x08\xaa"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "g0b\x0bZ)rM|a"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    list_1 = [list_0, list_0, list_0, bool_0]
    var_0 = module_0.func(*list_1)
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = 'K8"\rxJ|<mI\\&\t'
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_1.object(**var_0)


def test_case_5():
    str_0 = "a0)8S5ha&"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    int_0 = 1938
    dict_0 = {int_0: int_0, int_0: int_0}
    str_0 = "a8bj(8/5hh&"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_1.object(**dict_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "h0bj)V5ha&"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "h1blbV56ha\r"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = "h8<<y!*BB"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


def test_case_10():
    str_0 = "a15QH`5'$"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)