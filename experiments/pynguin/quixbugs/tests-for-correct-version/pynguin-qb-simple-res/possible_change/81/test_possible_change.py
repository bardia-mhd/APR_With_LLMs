# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0


def test_case_0():
    bool_0 = False
    var_0 = module_0.possible_change(bool_0, bool_0)
    assert var_0 == 1
    bool_1 = False
    var_1 = module_0.possible_change(bool_0, bool_0)
    assert var_1 == 1
    var_2 = module_0.possible_change(bool_0, bool_1)
    assert var_2 == 1
    var_3 = module_0.possible_change(bool_0, bool_0)
    assert var_3 == 1
    var_4 = module_0.possible_change(bool_0, bool_0)
    assert var_4 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "LUvj\np\x0bK;"
    dict_0 = {str_0: str_0, str_0: str_0}
    none_type_0 = None
    module_0.possible_change(dict_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -859
    var_0 = module_0.possible_change(int_0, int_0)
    assert var_0 == 0
    var_1 = module_0.possible_change(var_0, int_0)
    assert var_1 == 0
    var_2 = module_0.possible_change(int_0, var_0)
    assert var_2 == 1
    var_3 = module_0.possible_change(var_0, var_1)
    assert var_3 == 1
    var_4 = module_0.possible_change(var_1, var_3)
    assert var_4 == 0
    var_5 = module_0.possible_change(var_0, var_4)
    assert var_5 == 1
    var_6 = module_0.possible_change(var_0, var_5)
    assert var_6 == 0
    var_7 = module_0.possible_change(var_0, var_0)
    assert var_7 == 1
    module_0.possible_change(var_7, var_7)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 1501.714
    module_0.possible_change(float_0, float_0)