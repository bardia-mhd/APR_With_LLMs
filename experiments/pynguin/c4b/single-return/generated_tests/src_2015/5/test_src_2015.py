# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2015 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    bytes_0 = b'\r\xf3\x81\x10\xb0\xe8g"\xdc'
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 91


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xadN\xf6\xd6<Y\xe1c\x04\x08\x8a@\xe4j"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 273
    module_0.func(*var_0)


def test_case_3():
    bytes_0 = b'\r\xd4\x10\xb0\xe8g"\xdc'
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 28