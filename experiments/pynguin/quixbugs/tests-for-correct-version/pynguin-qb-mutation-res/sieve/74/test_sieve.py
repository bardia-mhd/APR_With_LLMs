# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sieve as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    var_0 = module_0.sieve(bool_0)
    module_0.sieve(var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x83C\x06\xd0\xed7|d\xad\x11h\xcb7\x9d\xf2"
    module_0.sieve(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 83
    var_0 = module_0.sieve(int_0)
    bool_0 = True
    var_1 = module_0.sieve(bool_0)
    module_0.sieve(var_1)