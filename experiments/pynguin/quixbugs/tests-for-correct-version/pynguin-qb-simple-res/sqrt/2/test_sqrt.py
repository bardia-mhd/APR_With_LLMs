# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sqrt as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 860
    var_0 = module_0.sqrt(int_0, int_0)
    assert var_0 == pytest.approx(36.752310811073265, abs=0.01, rel=0.01)
    var_1 = module_0.sqrt(var_0, int_0)
    assert var_1 == pytest.approx(18.376155405536633, abs=0.01, rel=0.01)
    var_2 = module_0.sqrt(var_0, var_0)
    assert var_2 == pytest.approx(6.897730965014528, abs=0.01, rel=0.01)
    var_3 = module_0.sqrt(int_0, int_0)
    assert var_3 == pytest.approx(36.752310811073265, abs=0.01, rel=0.01)
    var_4 = module_0.sqrt(var_3, var_3)
    assert var_4 == pytest.approx(6.897730965014528, abs=0.01, rel=0.01)
    var_5 = module_0.sqrt(var_4, var_3)
    assert var_5 == pytest.approx(3.448865482507264, abs=0.01, rel=0.01)
    none_type_0 = None
    bool_0 = False
    var_6 = module_0.sqrt(bool_0, var_2)
    assert var_6 == pytest.approx(0.0, abs=0.01, rel=0.01)
    var_7 = module_0.sqrt(var_5, var_5)
    assert var_7 == pytest.approx(1.724432741253632, abs=0.01, rel=0.01)
    module_0.sqrt(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    var_0 = module_0.sqrt(bool_0, bool_0)
    assert var_0 == pytest.approx(0.5, abs=0.01, rel=0.01)
    int_0 = 1502
    set_0 = {int_0}
    module_0.sqrt(set_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
    module_0.sqrt(list_0, list_0)