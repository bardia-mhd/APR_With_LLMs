# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2087 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "D$em4S.on`"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    tuple_0 = ()
    dict_0 = {}
    list_0 = [tuple_0, tuple_0, tuple_0, dict_0, dict_0]
    list_1 = [list_0, tuple_0]
    var_0 = module_0.func(*list_1)
    set_0 = {tuple_0}
    tuple_1 = (tuple_0, set_0)
    list_2 = [tuple_1, set_0]
    var_1 = module_0.func(*list_2)
    module_0.func()


def test_case_3():
    bytes_0 = b"SK\xe0#@c\xfaP\x05\xd1\xd9a\xe3\xea"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0]
    list_1 = [list_0, list_0]
    var_0 = module_0.func(*list_1)
    tuple_0 = ()
    dict_0 = {}
    list_2 = [tuple_0, tuple_0, tuple_0, dict_0]
    list_3 = [list_2, tuple_0]
    var_1 = module_0.func(*list_3)
    set_0 = {tuple_0}
    tuple_1 = (tuple_0, set_0)
    list_4 = [tuple_1, set_0]
    var_2 = module_0.func(*list_4)