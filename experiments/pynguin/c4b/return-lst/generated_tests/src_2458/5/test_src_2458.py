# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2458 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"@\x96\x13wZ\xe3\x0b\xf6f\\w0\x1b\xab"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"@\x96\x13w\xceZ\xe3B\xf6fw0\x1b\xab"
    var_0 = module_0.func(*bytes_0)
    module_0.func()