# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2451 as module_0


def test_case_0():
    str_0 = "d"
    list_0 = [str_0, str_0]
    list_1 = [list_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_1)


def test_case_1():
    list_0 = []
    list_1 = [list_0, list_0, list_0]
    var_0 = module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "dw1J"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    set_0 = set()
    bool_0 = False
    str_0 = "V02RO"
    tuple_0 = (bool_0, str_0)
    dict_0 = {bool_0: set_0, str_0: tuple_0}
    tuple_1 = (set_0, tuple_0, dict_0)
    list_0 = [tuple_1, tuple_1, tuple_1, tuple_1, tuple_1, tuple_0, tuple_0]
    list_1 = [list_0]
    var_0 = module_0.func(*list_1)
#    module_0.func()