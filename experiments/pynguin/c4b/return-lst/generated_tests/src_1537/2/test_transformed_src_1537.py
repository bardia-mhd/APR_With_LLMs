# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1537 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -98
    bool_0 = False
    list_0 = []
    tuple_0 = (int_0, bool_0, bool_0, list_0)
    list_1 = [tuple_0, tuple_0, bool_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    list_0 = [set_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "B"
    str_1 = 'iCNUoi"7_-'
    list_0 = [str_0, str_1]
    var_0 = module_0.func(*list_0)
    bool_0 = False
    dict_0 = {str_0: str_0, str_1: bool_0}
#    module_1.object(**dict_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ")\n|zj\x0bk\r`2wCA^"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    var_2 = module_0.func(*var_1)
    var_3 = module_0.func(*var_1)
#    module_0.func()