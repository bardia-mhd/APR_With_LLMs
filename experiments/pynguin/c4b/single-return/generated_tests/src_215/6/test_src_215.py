# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_215 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xa3{O\x02\x0eiE"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 7
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"(z\x02\xb0\t\x05?\xee"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 4
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xff2\x1c\xe1K"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 3
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x18l\xcb\x10A\x0c\xc4\xfe\r'.\x15\xea\"\x16"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 5
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"(\x02\xe9\xb0\t\x05?\xee"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 4
    bytes_1 = b"k\xf9\xb4\xfd\x00\x02R\x86]\xd3\xbc\xb5\xd8\x06\xfe@"
    var_1 = module_0.func(*bytes_1)
    assert var_1 == 0
    module_0.func()