# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kheapsort as module_0
import builtins as module_1


def test_case_0():
    none_type_0 = None
    var_0 = module_0.kheapsort(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "7XTW&qZrL71%*%"
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0]
    var_0 = module_0.kheapsort(tuple_0, str_0)
    int_0 = 2313
    var_1 = module_0.kheapsort(list_0, int_0)
    module_1.object(*var_1)


def test_case_2():
    str_0 = "7XTW&qZrL71%*%"
    var_0 = module_0.kheapsort(str_0, str_0)
    var_1 = module_0.kheapsort(str_0, str_0)
    tuple_0 = ()
    var_2 = module_0.kheapsort(str_0, str_0)
    list_0 = []
    var_3 = module_0.kheapsort(tuple_0, str_0)
    int_0 = 2318
    var_4 = module_0.kheapsort(int_0, var_0)
    var_5 = module_0.kheapsort(list_0, int_0)
    object_0 = module_1.object(*var_5)
    var_6 = module_0.kheapsort(var_5, object_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    var_0 = module_0.kheapsort(bool_0, bool_0)
    str_0 = "YW:wK gv}c^~VtI d"
    var_1 = module_0.kheapsort(bool_0, var_0)
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0]
    var_2 = module_0.kheapsort(tuple_0, str_0)
    var_3 = module_0.kheapsort(list_0, bool_0)
    bool_1 = False
    var_4 = module_0.kheapsort(var_0, bool_1)
    var_5 = module_0.kheapsort(var_2, var_4)
    module_1.object(*var_3)