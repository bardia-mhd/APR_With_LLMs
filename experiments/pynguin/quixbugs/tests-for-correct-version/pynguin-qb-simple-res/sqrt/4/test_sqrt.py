# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sqrt as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 3375
    var_0 = module_0.sqrt(int_0, int_0)
    assert var_0 == pytest.approx(72.50547472624932, abs=0.01, rel=0.01)
    var_1 = module_0.sqrt(int_0, int_0)
    assert var_1 == pytest.approx(72.50547472624932, abs=0.01, rel=0.01)
    var_2 = module_0.sqrt(var_0, var_1)
    assert var_2 == pytest.approx(11.458616660773616, abs=0.01, rel=0.01)
    var_3 = module_0.sqrt(var_1, var_2)
    assert var_3 == pytest.approx(8.893105360723723, abs=0.01, rel=0.01)
    bytes_0 = b"\x80\x98\xcf"
    module_0.sqrt(var_3, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.sqrt(bool_0, bool_0)
    assert var_0 == pytest.approx(0.0, abs=0.01, rel=0.01)
    module_0.sqrt(dict_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "q\x0bDo4*"
    module_1.object(**str_0)