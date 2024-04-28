# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sqrt as module_0


def test_case_0():
    int_0 = 3584
    var_0 = module_0.sqrt(int_0, int_0)
    assert var_0 == pytest.approx(75.85229371288418, abs=0.01, rel=0.01)


def test_case_1():
    int_0 = 441
    bool_0 = True
    bool_1 = False
    var_0 = module_0.sqrt(bool_1, bool_1)
    assert var_0 == pytest.approx(0.0, abs=0.01, rel=0.01)
    var_1 = module_0.sqrt(int_0, bool_0)
    assert var_1 == pytest.approx(21.000205541902297, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b""
    module_0.sqrt(bytes_0, bytes_0)