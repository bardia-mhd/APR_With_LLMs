# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1260 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "FiOO<WGd3oJ>&pX\x0bJyzl"
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    module_0.func(*bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b""
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)