# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2132 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    tuple_0 = (dict_0, bool_0)
    list_0 = [tuple_0, bool_0, bool_0, tuple_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"L\x9b\xd6\xac"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xf0\xd1\x97\xff\x1eZ\xffr\x9a\x1djE\x00\x81\xd2\\Dc\x0b"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    module_1.object(**var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "-x=1rrT+Jg5T@39"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()