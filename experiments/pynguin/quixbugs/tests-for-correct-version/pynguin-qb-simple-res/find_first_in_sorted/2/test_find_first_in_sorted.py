# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_first_in_sorted as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"F\x12\xa7\x82\x0c\xd9\xf6\tIt\xbc\xc3\xaf\xde{\xfa\xa9\xdd\xf7"
    set_0 = {bytes_0, bytes_0, bytes_0}
    module_0.find_first_in_sorted(set_0, set_0)


def test_case_1():
    set_0 = set()
    var_0 = module_0.find_first_in_sorted(set_0, set_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "g"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == 0
    var_1 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_1 == 0
    module_0.find_first_in_sorted(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"n\xfa\xf4\xa2\xc5"
    module_0.find_first_in_sorted(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "g"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.find_first_in_sorted(list_0, str_0)
    assert var_0 == 0
    bool_0 = False
    module_0.find_first_in_sorted(bool_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "\x0c(L |Lp%d68W;"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1
    module_0.find_first_in_sorted(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    bool_0 = True
    dict_0 = {}
    tuple_0 = (bool_0, bool_0, dict_0)
    bool_1 = True
    str_0 = ""
    tuple_1 = (tuple_0, bool_1, str_0)
    var_0 = module_0.find_first_in_sorted(tuple_1, bool_1)
    assert var_0 == 1
    none_type_0 = None
    module_0.find_first_in_sorted(none_type_0, none_type_0)