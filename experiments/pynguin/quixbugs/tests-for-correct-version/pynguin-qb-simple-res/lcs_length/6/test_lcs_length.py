# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "S!Aoo%S]\n}[0Na/9}C\n"
    var_0 = module_0.lcs_length(str_0, str_0)
    assert var_0 == 19
    str_1 = "YvisrJmj9"
    var_1 = module_0.lcs_length(str_1, str_1)
    assert var_1 == 9
    module_0.lcs_length(str_1, var_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    var_0 = module_0.lcs_length(set_0, set_0)
    assert var_0 == 0
    none_type_0 = None
    module_0.lcs_length(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x86\x9aX\xf6\xcb\xc8M"
    str_0 = "L\\}s)2/_>9SWT!?K!&"
    dict_0 = {bytes_0: bytes_0, str_0: str_0, str_0: str_0}
    float_0 = 2215.178474
    module_0.lcs_length(dict_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 1634.635
    module_0.lcs_length(float_0, float_0)