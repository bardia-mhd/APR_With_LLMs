# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2264 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "XiA*72b)Azz@Pi"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = "X{z1v\t[~+>h-z47w4"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "X}z1v7x[~+>h-zZ47w4"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


def test_case_4():
    str_0 = "X7z1v\t[h4W4Z4z47w4"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    object_0 = module_1.object()
    var_2 = module_0.func(*list_0)