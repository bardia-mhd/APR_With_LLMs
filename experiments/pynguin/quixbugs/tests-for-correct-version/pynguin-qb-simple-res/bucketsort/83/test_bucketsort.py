# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bucketsort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    module_0.bucketsort(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    dict_0 = {}
    var_0 = module_0.bucketsort(dict_0, bool_0)
    module_0.bucketsort(bool_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 2051
    str_0 = "6T t&:!@[A:t{k\t4m\\"
    module_0.bucketsort(str_0, int_0)