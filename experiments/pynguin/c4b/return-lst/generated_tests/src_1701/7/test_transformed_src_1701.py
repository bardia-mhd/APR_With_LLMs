# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1701 as module_0


def test_case_0():
    str_0 = "5\t_u\x0b dq\x0b`k+i"
    var_0 = module_0.func(*str_0)


def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)


def test_case_4():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*var_1)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "4tMfDP"
    var_0 = module_0.func(*str_0)
#    module_0.func()