# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bucketsort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    bool_1 = False
    list_0 = [bool_0, bool_1, bool_1]
    int_0 = -452
    module_0.bucketsort(list_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.bucketsort(none_type_0, none_type_0)


def test_case_2():
    bool_0 = False
    bool_1 = True
    list_0 = [bool_0, bool_1, bool_1]
    int_0 = 1104
    var_0 = module_0.bucketsort(list_0, int_0)