# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1541 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"E\x8d\x01\xfeN\xd2A\x89J\x1e\x9b"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 78
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"3\xdd\x0f[g_\x1d<\xfd\xa5"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 9
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xcc\x8b\x8a\x16\xc3\xd3\x0e\xfd~\xec\xcb\xfcE\xfb\xbeV\xd5\xf0"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 10
    module_0.func()