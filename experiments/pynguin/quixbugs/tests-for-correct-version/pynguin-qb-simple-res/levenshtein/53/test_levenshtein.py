# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import levenshtein as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "U9r;"
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0
    module_0.levenshtein(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -3182
    module_0.levenshtein(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xb1\x0b\xae\x86\xcamf\xcc\xa9"
    module_0.levenshtein(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    tuple_0 = ()
    bytes_0 = b"q7\xa9\xe0n\x9f+l"
    str_0 = ",7\x0cq(Xtc@jxNu^OXU"
    bytes_1 = b"+\xb2\xa6\xe9\xfd\xd7\x1b\xc2\xa9\no\xa0)"
    dict_0 = {tuple_0: str_0, tuple_0: str_0, str_0: bytes_1}
    int_0 = 491
    tuple_1 = (tuple_0, bytes_0, dict_0, int_0)
    module_0.levenshtein(tuple_1, bytes_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "i+m"
    str_1 = "c!g^hyWo\x0c8hDof(="
    var_0 = module_0.levenshtein(str_0, str_1)
    assert var_0 == 16
    var_1 = module_0.levenshtein(str_0, str_0)
    assert var_1 == 0
    int_0 = -2697
    module_0.levenshtein(str_0, int_0)