# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0
import builtins as module_1


def test_case_0():
    bool_0 = False
    var_0 = module_0.possible_change(bool_0, bool_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    module_0.possible_change(dict_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -3224
    none_type_0 = None
    var_0 = module_0.possible_change(none_type_0, int_0)
    assert var_0 == 0
    var_1 = module_0.possible_change(int_0, int_0)
    assert var_1 == 0
    object_0 = module_1.object()
    bool_0 = True
    var_2 = module_0.possible_change(var_1, bool_0)
    assert var_2 == 0
    tuple_0 = (var_1, object_0)
    object_1 = module_1.object()
    module_0.possible_change(object_1, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    module_0.possible_change(bool_0, bool_0)