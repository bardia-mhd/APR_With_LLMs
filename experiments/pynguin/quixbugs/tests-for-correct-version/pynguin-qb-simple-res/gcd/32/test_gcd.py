# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import gcd as module_0


def test_case_0():
    float_0 = 853.8
    var_0 = module_0.gcd(float_0, float_0)
    assert var_0 == pytest.approx(853.8, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.gcd(none_type_0, none_type_0)