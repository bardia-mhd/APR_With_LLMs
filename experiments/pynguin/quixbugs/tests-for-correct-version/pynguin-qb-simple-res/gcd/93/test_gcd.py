# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import gcd as module_0


def test_case_0():
    int_0 = 994
    var_0 = module_0.gcd(int_0, int_0)
    assert var_0 == 994
    var_1 = module_0.gcd(var_0, int_0)
    assert var_1 == 994


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xb1\xcd}m"
    module_0.gcd(bytes_0, bytes_0)