# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0


def test_case_0():
    bool_0 = False
    dict_0 = {bool_0: bool_0}
    var_0 = module_0.lcs_length(dict_0, dict_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ""
    var_0 = module_0.lcs_length(str_0, str_0)
    assert var_0 == 0
    module_0.lcs_length(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xae\xb4\xd3<\x9a\xf9\x9f \xf0\x05\x8a\x02J-4c "
    none_type_0 = None
    module_0.lcs_length(bytes_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    module_0.lcs_length(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    str_0 = "jPfbJUcx\tQ'bW"
    complex_0 = 123.93196 - 538.7624j
    tuple_0 = (bool_0, str_0, bool_0, complex_0)
    var_0 = module_0.lcs_length(tuple_0, tuple_0)
    assert var_0 == 4
    none_type_0 = None
    module_0.lcs_length(none_type_0, none_type_0)