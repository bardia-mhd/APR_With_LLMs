# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_370 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    bytes_0 = b"\xc3?\xe2\xef*m\xbbq\xadXCr\xc7\r"
    var_0 = module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xe58^\xabu\x99\xea\xb0\xed"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b".\xe7\xbf\x07\xcf\xc1%\xee\xbd\x08M\xf9\x06\x9b\x94^"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xe5?\xbe \x00\x1e"
    var_0 = module_0.func(*bytes_0)
    list_0 = [bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)