# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0


def test_case_0():
    str_0 = "r&Y5u)`WI-%62SMP,\n^$"
    var_0 = module_0.lcs_length(str_0, str_0)
    assert var_0 == 20


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 466
    module_0.lcs_length(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = " @"
    var_0 = module_0.lcs_length(str_0, str_0)
    assert var_0 == 2
    complex_0 = -1397.27 - 1138.73j
    list_0 = [complex_0, complex_0, complex_0]
    int_0 = 101
    set_0 = {int_0}
    var_1 = module_0.lcs_length(list_0, str_0)
    assert var_1 == 0
    module_0.lcs_length(list_0, set_0)