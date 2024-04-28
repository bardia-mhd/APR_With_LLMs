# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sqrt as module_0


def test_case_0():
    float_0 = 1419.5747
    var_0 = module_0.sqrt(float_0, float_0)
    assert var_0 == pytest.approx(40.27762394259008, abs=0.01, rel=0.01)
    var_1 = module_0.sqrt(var_0, var_0)
    assert var_1 == pytest.approx(7.354024824311992, abs=0.01, rel=0.01)
    var_2 = module_0.sqrt(var_0, var_1)
    assert var_2 == pytest.approx(6.415487254492299, abs=0.01, rel=0.01)
    var_3 = module_0.sqrt(var_1, var_1)
    assert var_3 == pytest.approx(3.677012412155996, abs=0.01, rel=0.01)


def test_case_1():
    bool_0 = True
    var_0 = module_0.sqrt(bool_0, bool_0)
    assert var_0 == pytest.approx(0.5, abs=0.01, rel=0.01)