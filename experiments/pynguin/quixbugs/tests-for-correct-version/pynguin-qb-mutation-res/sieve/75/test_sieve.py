# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sieve as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1485
    var_0 = module_0.sieve(int_0)
    var_1 = module_0.sieve(int_0)
    var_2 = module_0.sieve(int_0)
    int_1 = 1579
    var_3 = module_0.sieve(int_1)
    bool_0 = True
    var_4 = module_0.sieve(bool_0)
    var_5 = module_0.sieve(int_1)
    var_6 = module_0.sieve(bool_0)
    module_0.sieve(var_6)


def test_case_1():
    bool_0 = True
    var_0 = module_0.sieve(bool_0)
    var_1 = module_0.sieve(bool_0)