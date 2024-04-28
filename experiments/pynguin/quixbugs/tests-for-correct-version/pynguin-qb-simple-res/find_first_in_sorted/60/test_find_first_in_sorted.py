# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_first_in_sorted as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    set_0 = set()
    list_0 = [set_0, set_0]
    module_0.find_first_in_sorted(list_0, list_0)


def test_case_1():
    list_0 = []
    var_0 = module_0.find_first_in_sorted(list_0, list_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 937.62
    module_0.find_first_in_sorted(float_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"P\xa63\xed\xae\xbd\x862\xf5"
    bytes_1 = b"\x9d\x1d\xc9\x81"
    tuple_0 = (bytes_0, bytes_1)
    var_0 = module_0.find_first_in_sorted(tuple_0, bytes_1)
    assert var_0 == 1
    set_0 = set()
    module_0.find_first_in_sorted(var_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "{)D5[Xl~l8+A/f"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1
    int_0 = -195
    dict_0 = {int_0: int_0}
    tuple_0 = (int_0, int_0, dict_0)
    module_0.find_first_in_sorted(var_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "X"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == 0
    none_type_0 = None
    str_1 = "RHSwp,may9L!6FL"
    str_2 = "&r9#D"
    str_3 = "&B o4),H^'77~"
    dict_0 = {str_1: str_1, str_2: none_type_0, str_3: str_2}
    module_1.object(**dict_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "-,/51R@< U"
    list_0 = [str_0, str_0]
    var_0 = module_0.find_first_in_sorted(list_0, str_0)
    assert var_0 == 0
    list_1 = [list_0, list_0, str_0]
    var_1 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_1 == -1
    module_0.find_first_in_sorted(list_1, var_1)