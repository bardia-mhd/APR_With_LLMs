# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import levenshtein as module_0


def test_case_0():
    str_0 = "O"
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -1528.197
    module_0.levenshtein(float_0, float_0)


def test_case_2():
    str_0 = "akT:81rLr-F"
    str_1 = ';~\n"'
    var_0 = module_0.levenshtein(str_1, str_0)
    assert var_0 == 11
    var_1 = module_0.levenshtein(str_0, str_1)
    assert var_1 == 11