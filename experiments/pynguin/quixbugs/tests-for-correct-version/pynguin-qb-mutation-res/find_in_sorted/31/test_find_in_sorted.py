# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_in_sorted as module_0
import builtins as module_1


def test_case_0():
    str_0 = "iK\\}?AHED/"
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1
    dict_0 = {var_0: var_0, var_0: var_0, var_0: var_0}
    tuple_0 = (dict_0, var_0)
    var_1 = module_0.find_in_sorted(tuple_0, var_0)
    assert var_1 == 1
    str_1 = '{{ *R2\tz"33phQ'
    var_2 = module_0.find_in_sorted(str_1, str_1)
    assert var_2 == -1


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    object_0 = module_1.object()
    dict_0 = {bool_0: object_0}
    none_type_0 = None
    module_0.find_in_sorted(dict_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.find_in_sorted(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "\r>P@ToRD}q|a\r$Q2i"
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1
    bool_0 = True
    module_0.find_in_sorted(bool_0, bool_0)