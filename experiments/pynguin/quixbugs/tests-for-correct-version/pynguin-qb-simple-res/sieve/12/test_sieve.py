# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sieve as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 2946
    var_0 = module_0.sieve(int_0)
    bool_0 = False
    var_1 = module_0.sieve(bool_0)
    module_0.sieve(var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -3458
    var_0 = module_0.sieve(int_0)
    bytes_0 = b"8\x103OnU\xbcL"
    module_0.sieve(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    complex_0 = -2344.21222 - 5734.93j
    list_0 = [complex_0]
    module_0.sieve(list_0)