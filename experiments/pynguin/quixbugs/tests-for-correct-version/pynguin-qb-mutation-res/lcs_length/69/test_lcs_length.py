# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "DjV5Jmt,\x0b!2D\\=A6&]"
    var_0 = module_0.lcs_length(str_0, str_0)
    assert var_0 == 18
    module_0.lcs_length(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    var_0 = module_0.lcs_length(set_0, set_0)
    assert var_0 == 0
    var_1 = module_0.lcs_length(set_0, var_0)
    assert var_1 == 0
    module_0.lcs_length(var_0, var_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.lcs_length(bool_0, bool_0)