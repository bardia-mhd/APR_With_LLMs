# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2118 as module_0


def test_case_0():
    bool_0 = False
    bytes_0 = b"8\xcf`\x11\x8d\x1a58F"
    list_0 = [bool_0, bool_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 1421
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    bytes_0 = b"//y"
    var_1 = module_0.func(*bytes_0)
    module_0.func()