# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_479 as module_0


def test_case_0():
    bytes_0 = b"\x96\x0c\x9e\x1d\x0fJ\xc9j\x84\x1cO\xe9\xa9\x86K\xbd\x86\x1dI\xdc"
    str_0 = 'RB\x0b?R-^K]~Ooc"!%Vx}'
    list_0 = [bytes_0, bytes_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xfc\xdbPQ\xbb\xe0\x8d?k\xb3\x89\xfa\x07\xd8J\xa1"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    list_1 = [var_0, list_0, bytes_0, var_0]
    var_1 = module_0.func(*list_1)
    module_0.func()