# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bucketsort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -719
    tuple_0 = (int_0,)
    module_0.bucketsort(tuple_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.bucketsort(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    set_0 = set()
    var_0 = module_0.bucketsort(set_0, bool_0)
    int_0 = -719
    var_1 = module_0.bucketsort(var_0, int_0)
    module_0.bucketsort(set_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    set_0 = set()
    var_0 = module_0.bucketsort(set_0, bool_0)
    int_0 = -719
    tuple_0 = module_0.bucketsort(var_0, int_0)
    var_1 = module_0.bucketsort(tuple_0, int_0)
    var_2 = module_0.bucketsort(var_1, int_0)
    module_0.bucketsort(int_0, tuple_0)