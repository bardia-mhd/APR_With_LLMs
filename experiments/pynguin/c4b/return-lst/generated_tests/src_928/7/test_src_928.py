# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_928 as module_0


def test_case_0():
    int_0 = 0
    bool_0 = False
    bytes_0 = b"\xfb\x1b\xed\xca\xe1S\xe9PL\x9dvBg\x95\x84\xaf"
    dict_0 = {}
    bytes_1 = b"S&\xf9i\xd7,=sr\x10\xf9_"
    tuple_0 = (bytes_0, dict_0, dict_0, bytes_1)
    tuple_1 = (int_0, bool_0, tuple_0)
    var_0 = module_0.func(*tuple_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()