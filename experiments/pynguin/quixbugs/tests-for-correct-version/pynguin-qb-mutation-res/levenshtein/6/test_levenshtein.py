# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import levenshtein as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = ";7rl"
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0
    float_0 = -1327.8
    module_0.levenshtein(float_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0, none_type_0]
    module_0.levenshtein(none_type_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -2266.4
    set_0 = {float_0}
    int_0 = 901
    tuple_0 = (set_0, int_0, int_0)
    module_0.levenshtein(tuple_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Dmf{u9A>=\\Q"
    str_1 = "Dmf{99A>=\\Q"
    var_0 = module_0.levenshtein(str_0, str_1)
    assert var_0 == 1
    object_0 = module_1.object()
    module_0.levenshtein(object_0, str_0)