# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bucketsort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 237
    dict_0 = {}
    tuple_0 = (int_0, int_0, dict_0)
    module_0.bucketsort(tuple_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 1042
    module_0.bucketsort(int_0, int_0)


def test_case_2():
    int_0 = 237
    dict_0 = {}
    var_0 = module_0.bucketsort(dict_0, int_0)