# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import longest_common_subsequence as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 3641
    module_0.longest_common_subsequence(int_0, int_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(none_type_0, none_type_0)
    assert var_0 == ""


def test_case_2():
    object_0 = module_1.object()
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(object_0, none_type_0)
    assert var_0 == ""


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x96\xc9\x9f\xfbN\xbe\xf8\xea\x8d\x1e"
    module_0.longest_common_subsequence(bytes_0, bytes_0)


def test_case_4():
    complex_0 = -279.2 + 330.795j
    set_0 = {complex_0, complex_0, complex_0, complex_0}
    str_0 = "/@~|M\rNju.YNtTp)"
    tuple_0 = (complex_0, set_0, str_0)
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(complex_0, none_type_0)
    assert var_0 == ""
    var_1 = module_0.longest_common_subsequence(tuple_0, str_0)
    assert var_1 == ""