# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1133 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"B\x7fre\xe0\xdbu\xd1\xaa\x0c\xf3W\x018\x85<\xd6"
    list_0 = [bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b""
    list_0 = [bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)