# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1903 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x0bQ\x9d\x8b\xf8TX{\x8e\x8a\xba\xc3\x85"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


def test_case_2():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    dict_1 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: dict_0}
    tuple_0 = (dict_1, dict_1, dict_0, dict_1)
    list_0 = [tuple_0, dict_1, bool_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    list_0 = []
    list_1 = [list_0]
    var_0 = module_0.func(*list_1)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xb8c\x19"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0]
    list_1 = [list_0, list_0]
    var_0 = module_0.func(*list_1)
    var_1 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = ""
    bool_0 = False
    list_0 = [bool_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0, bool_0, bool_0]
    list_1 = [list_0, str_0, bool_0]
    var_0 = module_0.func(*list_1)
    module_0.func()