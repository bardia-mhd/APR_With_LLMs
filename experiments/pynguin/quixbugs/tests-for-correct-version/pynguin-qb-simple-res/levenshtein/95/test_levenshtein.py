# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import levenshtein as module_0


def test_case_0():
    str_0 = ""
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = 406.8
    module_0.levenshtein(float_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x1b\x9a^ =$\xbf\x05S\xcc\xcf*\xf2\xf1\xab"
    module_0.levenshtein(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "X-sAM2y/cP;"
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0
    tuple_0 = (var_0, var_0, var_0)
    module_0.levenshtein(tuple_0, str_0)