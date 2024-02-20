# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kheapsort as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"h|X\x9cl\xfdF\x1a\x01\x1b\x9cH\xc3"
    var_0 = module_0.kheapsort(bytes_0, bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0]
    none_type_0 = None
    var_0 = module_0.kheapsort(list_0, none_type_0)
    var_1 = module_0.kheapsort(list_0, bool_0)
    var_2 = module_0.kheapsort(bool_0, list_0)
    var_3 = module_0.kheapsort(var_0, var_2)
    var_4 = module_0.kheapsort(var_1, var_1)
    var_5 = module_0.kheapsort(none_type_0, var_0)
    var_6 = module_0.kheapsort(var_2, var_1)
    var_7 = module_0.kheapsort(none_type_0, var_0)
    var_8 = module_0.kheapsort(var_4, var_2)
#    module_1.object(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0]
    none_type_0 = None
    var_0 = module_0.kheapsort(list_0, none_type_0)
    none_type_1 = None
    var_1 = module_0.kheapsort(list_0, none_type_1)
    var_2 = module_0.kheapsort(var_0, var_0)
    var_3 = module_0.kheapsort(list_0, bool_0)
    var_4 = module_0.kheapsort(bool_0, list_0)
    var_5 = module_0.kheapsort(var_1, var_3)
    none_type_2 = None
    var_6 = module_0.kheapsort(var_3, var_3)
    var_7 = module_0.kheapsort(none_type_1, none_type_1)
    var_8 = module_0.kheapsort(var_0, bool_0)
    var_9 = module_0.kheapsort(none_type_2, none_type_2)
    var_10 = module_1.object()
    var_11 = module_0.kheapsort(var_4, var_3)
    var_12 = module_0.kheapsort(list_0, none_type_2)
    none_type_3 = None
    var_13 = module_0.kheapsort(var_9, var_4)
    var_14 = module_0.kheapsort(none_type_3, none_type_3)
    var_15 = module_0.kheapsort(var_14, var_0)
    var_16 = module_0.kheapsort(var_12, var_13)
#    module_1.object(*var_3)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    none_type_0 = None
    var_0 = module_0.kheapsort(list_0, none_type_0)
    var_1 = module_0.kheapsort(list_0, bool_0)
    var_2 = module_0.kheapsort(bool_0, list_0)
    var_3 = module_0.kheapsort(var_0, var_2)
    var_4 = module_0.kheapsort(var_1, var_1)
    var_5 = module_0.kheapsort(var_0, list_0)
    var_6 = module_1.object()
    var_7 = module_0.kheapsort(var_2, var_1)
    var_8 = module_0.kheapsort(none_type_0, var_0)
    var_9 = module_0.kheapsort(var_4, var_2)
#    module_1.object(*var_0)
