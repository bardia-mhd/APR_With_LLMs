# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_765 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    bool_0 = False
    int_0 = -2109
    bytes_0 = b"\xcb\x95\x0bU\xc8\xe6\x05"
    bool_1 = False
    tuple_0 = (bool_0, int_0, bytes_0, bool_1)
    list_0 = [bool_0, bool_0, tuple_0, bool_1]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    str_0 = "wTZqV}g15 .:H"
    list_0 = [bool_0, str_0]
    var_0 = module_0.func(*list_0)
    list_1 = []
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x88\xc0"
    var_0 = module_0.func(*bytes_0)
    module_0.func()