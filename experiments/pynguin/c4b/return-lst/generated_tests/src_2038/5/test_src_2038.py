# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2038 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xabc}\xe3Q\xad\xcd"
    module_0.func(*bytes_0)


def test_case_1():
    bytes_0 = b"l\xe1\xe2#\xf6\xfa\x12\xce@\xe5l\x80\xfc"
    var_0 = module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b",\xec\t\x01\x94\xb8\xe9\x04\x8c^"
    module_0.func(*bytes_0)