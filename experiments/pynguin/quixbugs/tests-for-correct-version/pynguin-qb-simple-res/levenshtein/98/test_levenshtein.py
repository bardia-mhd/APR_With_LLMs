# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import levenshtein as module_0


def test_case_0():
    str_0 = "DcW&"
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "DcW&"
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0
    int_0 = 1285
    list_0 = [str_0, var_0, int_0]
    module_0.levenshtein(str_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b";\xb8\x14\x13Y\x0c"
    str_0 = "'l\x0cSU,f&$~Og;X"
    module_0.levenshtein(bytes_0, str_0)