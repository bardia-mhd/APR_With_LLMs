# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import gcd as module_0


def test_case_0():
    int_0 = 1578
    var_0 = module_0.gcd(int_0, int_0)
    assert var_0 == 1578


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x1f\xe2Z\x0b\x89\xf2\xd2\x90\x0f8\xe9"
#    module_0.gcd(bytes_0, bytes_0)
