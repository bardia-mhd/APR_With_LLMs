# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_first_in_sorted as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xc6n4\xf0\xe6\xa1\xde"
    list_0 = [bytes_0, bytes_0, bytes_0]
    none_type_0 = None
    module_0.find_first_in_sorted(list_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    none_type_0 = None
    list_0 = []
    int_0 = 623
    var_0 = module_0.find_first_in_sorted(list_0, int_0)
    assert var_0 == -1
    bool_1 = False
    tuple_0 = (list_0, bool_0, list_0, bool_1)
    module_0.find_first_in_sorted(none_type_0, tuple_0)


def test_case_2():
    pass


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "~"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == 0
    module_0.find_first_in_sorted(var_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 2112.076
    list_0 = [float_0, float_0]
    var_0 = module_0.find_first_in_sorted(list_0, float_0)
    assert var_0 == 0
    module_0.find_first_in_sorted(float_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "d_S{mkX"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1
    int_0 = -1970
    str_1 = "\x0b"
    str_2 = "phm<\x0cz[w\t9N\x0bR\x0cE@HS|-"
    dict_0 = {str_0: int_0, str_1: str_1, str_2: int_0}
    module_1.object(**dict_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    int_0 = 550
    str_0 = "\np"
    tuple_0 = (str_0, int_0)
    tuple_1 = (int_0, tuple_0)
    var_0 = module_0.find_first_in_sorted(tuple_1, tuple_0)
    assert var_0 == 1
    none_type_0 = None
    module_0.find_first_in_sorted(none_type_0, none_type_0)