# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import levenshtein as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "\\zwIQi [U_NuLq"
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0
    object_0 = module_1.object()
    set_0 = {object_0}
    module_0.levenshtein(set_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.levenshtein(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -850
    str_0 = "$}A&$MpKnCt"
    bool_0 = False
    float_0 = -1924.0
    tuple_0 = (bool_0, float_0)
    tuple_1 = (int_0, str_0, tuple_0)
    module_0.levenshtein(tuple_1, str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xbap\x14<\x86"
    module_0.levenshtein(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"s\xd4\xbau\xce\xd0l\xc8\xb6l6:\xf2l&tW\xac5'"
    list_0 = [bytes_0]
    module_0.levenshtein(list_0, bytes_0)