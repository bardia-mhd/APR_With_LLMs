# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2613 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xc7\xae\n\x01\xb6\xd6\xe4\xe1\x80\x82\xc0\xa0~~\x1c\xa3"
    list_0 = [bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.func(*none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -1833.94
    dict_0 = {}
    tuple_0 = (float_0, dict_0)
    list_0 = [dict_0, tuple_0, dict_0, dict_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "\x0cKR+,iC6Y\\<@Os(bS5"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "V"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()