# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sieve as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1973
    var_0 = module_0.sieve(int_0)
    var_1 = module_0.sieve(int_0)
    var_2 = module_0.sieve(int_0)
    module_0.sieve(var_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.sieve(none_type_0)