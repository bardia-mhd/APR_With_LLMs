# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"L\xaf\xb8N\xd5\x88f^\xdc\xbdO\x9f\xd69t\xc0"
    module_0.knapsack(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    str_0 = ";"
    var_0 = module_0.knapsack(str_0, list_0)
    assert var_0 == 0
    module_0.knapsack(str_0, str_0)


def test_case_2():
    bool_0 = False
    bytes_0 = b"\xaf"
    dict_0 = {
        bool_0: bytes_0,
        bool_0: bytes_0,
        bool_0: bool_0,
        bool_0: bool_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
    }
    dict_1 = {bool_0: dict_0}
    var_0 = module_0.knapsack(bool_0, dict_1)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    bytes_0 = b""
    dict_0 = {
        bool_0: bytes_0,
        bool_0: bytes_0,
        bool_0: bytes_0,
        bool_0: bool_0,
        bool_0: bool_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
    }
    dict_1 = {bool_0: dict_0}
    bool_1 = True
    module_0.knapsack(bool_1, dict_1)


def test_case_4():
    bool_0 = True
    bytes_0 = b"\x1b\x07"
    tuple_0 = (bytes_0,)
    var_0 = module_0.knapsack(bool_0, tuple_0)
    assert var_0 == 0