# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2038 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    bytes_0 = b"\x84\xc2\xc3\x05\xb3\xcb\xcd"
    var_0 = module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xa3\x9f\xe3\xdb\x17+\xf7\x0c\xf2\xa8\xb7\xa1<i\x84-"
    module_0.func(*bytes_0)


def test_case_3():
    bytes_0 = b"\x83\xc2\xc3\x05\xf8\xb6\xc6tc\x01\xcd"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_1.object()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xea\x01'\xb0\x0c\xc7e\x14'\x12\xa6"
    module_0.func(*bytes_0)