# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import subsequences as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    none_type_0 = None
    var_0 = module_0.subsequences(bool_0, none_type_0, bool_0)
    none_type_1 = None
    module_0.subsequences(none_type_1, none_type_1, none_type_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.subsequences(none_type_0, none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    none_type_0 = None
    int_0 = 468
    var_0 = module_0.subsequences(bool_0, int_0, int_0)
    module_0.subsequences(var_0, int_0, none_type_0)


def test_case_3():
    int_0 = 401
    var_0 = module_0.subsequences(int_0, int_0, int_0)