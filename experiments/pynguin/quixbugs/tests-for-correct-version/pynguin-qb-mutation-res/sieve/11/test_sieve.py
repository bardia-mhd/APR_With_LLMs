# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sieve as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1370
    var_0 = module_0.sieve(int_0)
    var_1 = module_0.sieve(int_0)
    bytes_0 = b"\xa2\xcf\x80"
    tuple_0 = (var_1, bytes_0)
    module_0.sieve(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    complex_0 = -251 - 1248.025j
    set_0 = {complex_0, complex_0}
    list_0 = [complex_0, set_0, complex_0]
    module_0.sieve(list_0)