# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_first_in_sorted as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "tmXgB0KI/n[CGt\tav"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1
    none_type_0 = None
    module_0.find_first_in_sorted(none_type_0, none_type_0)


def test_case_1():
    bytes_0 = b"\x0c\t\x89\x05p~\xd1"
    tuple_0 = ()
    var_0 = module_0.find_first_in_sorted(tuple_0, bytes_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_2():
    object_0 = module_1.object()
    module_0.find_first_in_sorted(object_0, object_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    tuple_0 = (bool_0, bool_0, bool_0, bool_0)
    list_0 = [bool_0, tuple_0, tuple_0]
    var_0 = module_0.find_first_in_sorted(list_0, tuple_0)
    assert var_0 == 1
    module_0.find_first_in_sorted(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 3052.3567
    bool_0 = False
    tuple_0 = (float_0, bool_0, bool_0, bool_0)
    list_0 = [float_0, tuple_0, tuple_0]
    var_0 = module_0.find_first_in_sorted(tuple_0, bool_0)
    assert var_0 == 1
    module_0.find_first_in_sorted(list_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    tuple_0 = ()
    var_0 = module_0.find_first_in_sorted(tuple_0, tuple_0)
    assert var_0 == -1
    str_0 = "Q"
    var_1 = module_0.find_first_in_sorted(tuple_0, tuple_0)
    assert var_1 == -1
    dict_0 = {}
    var_2 = module_0.find_first_in_sorted(dict_0, dict_0)
    assert var_2 == -1
    var_3 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_3 == 0
    none_type_0 = None
    module_0.find_first_in_sorted(none_type_0, none_type_0)