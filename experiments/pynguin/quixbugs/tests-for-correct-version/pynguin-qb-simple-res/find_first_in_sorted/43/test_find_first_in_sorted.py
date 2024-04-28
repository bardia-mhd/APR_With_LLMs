# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_first_in_sorted as module_0


def test_case_0():
    str_0 = "9&Vp\t_b+9<"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    var_0 = module_0.find_first_in_sorted(tuple_0, tuple_0)
    assert var_0 == -1
    none_type_0 = None
    module_0.find_first_in_sorted(var_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 327
    module_0.find_first_in_sorted(int_0, int_0)


def test_case_3():
    bool_0 = False
    tuple_0 = (bool_0,)
    var_0 = module_0.find_first_in_sorted(tuple_0, bool_0)
    assert var_0 == 0
    var_1 = module_0.find_first_in_sorted(tuple_0, var_0)
    assert var_1 == 0


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    str_0 = '-!M\x0ct".sefBwA'
    tuple_0 = (bool_0, bool_0, str_0, bool_0)
    var_0 = module_0.find_first_in_sorted(tuple_0, str_0)
    assert var_0 == 2
    module_0.find_first_in_sorted(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = '-!M\x0ct".sefBwA'
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1
    tuple_0 = (str_0, str_0, str_0, str_0)
    var_1 = module_0.find_first_in_sorted(tuple_0, str_0)
    assert var_1 == 0
    module_0.find_first_in_sorted(tuple_0, var_1)