# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1478 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    bytes_0 = b"\xdaa\xdb\xb0\xa9\xc9\x88"
    var_0 = module_0.func(*bytes_0)


def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    bytes_0 = b"\\Eh\xdf\xf5O\x89"
    var_0 = module_0.func(*bytes_0)


def test_case_4():
    int_0 = 70
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)


def test_case_5():
    int_0 = 43
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    int_1 = -1180
    list_1 = [int_1, int_1]
    var_1 = module_0.func(*list_1)


def test_case_6():
    int_0 = 44
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    int_1 = -1180
    list_1 = [int_1, int_1]
    var_1 = module_0.func(*list_1)