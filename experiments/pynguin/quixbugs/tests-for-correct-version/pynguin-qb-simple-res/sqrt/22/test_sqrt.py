# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sqrt as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "1eV=F`m6\rF,^p@"
    int_0 = 3934
    var_0 = module_0.sqrt(int_0, int_0)
    assert var_0 == pytest.approx(81.43940201711064, abs=0.01, rel=0.01)
    var_1 = module_0.sqrt(var_0, var_0)
    assert var_1 == pytest.approx(12.586291638008456, abs=0.01, rel=0.01)
    module_0.sqrt(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    int_0 = 2729
    var_0 = module_0.sqrt(bool_0, int_0)
    assert var_0 == pytest.approx(0.0, abs=0.01, rel=0.01)
    module_0.sqrt(dict_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "-\x0cwLW{"
    module_0.sqrt(str_0, str_0)