# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0


def test_case_0():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    bool_1 = True
    tuple_0 = (bool_1, bool_0)
    bool_2 = False
    tuple_1 = (dict_0, tuple_0, bool_2)
    var_0 = module_0.possible_change(tuple_1, bool_2)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    module_0.possible_change(set_0, set_0)


def test_case_2():
    int_0 = -11
    var_0 = module_0.possible_change(int_0, int_0)
    assert var_0 == 0
    var_1 = module_0.possible_change(var_0, int_0)
    assert var_1 == 0


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    none_type_0 = None
    var_0 = module_0.possible_change(none_type_0, bool_0)
    assert var_0 == 0
    var_1 = module_0.possible_change(var_0, bool_0)
    assert var_1 == 0
    int_0 = 3899
    bool_1 = True
    module_0.possible_change(int_0, bool_1)