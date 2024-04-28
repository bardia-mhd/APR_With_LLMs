# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import levenshtein as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "de]hoJN2 V@[~MOqe\x0c"
    int_0 = -1693
    tuple_0 = (int_0, int_0, int_0, int_0)
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0
    module_0.levenshtein(str_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xc2;U\xdb\x9c\xdd\x1d\xfad\nV\x14\xb9\xa2\xe3`\xab\xf5\x85"
    module_0.levenshtein(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xb3D6\xcfL(\xe8\x16\x1a\xa1;r\x8fa\x9f\xc3\x1f"
    list_0 = [bytes_0, bytes_0, bytes_0]
    module_0.levenshtein(list_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "jB/ \tm7KjIS6M0$"
    str_1 = "`?~."
    var_0 = module_0.levenshtein(str_0, str_1)
    assert var_0 == 15
    var_1 = module_0.levenshtein(str_1, str_1)
    assert var_1 == 0
    object_0 = module_1.object()
    module_0.levenshtein(var_1, var_1)