# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2330 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    set_0 = set()
    list_0 = [set_0, set_0, set_0, set_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = ")`"
    int_0 = -2333
    dict_0 = {str_0: int_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == ")`"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "\tY"
    int_0 = -2333
    dict_0 = {str_0: int_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == "\tY"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "\tY"
    int_0 = -2333
    dict_0 = {str_0: int_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == "\tY"
    var_1 = module_0.func(*str_0)
#    module_1.object(**var_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "a8"
    var_0 = module_0.func(*str_0)
    assert var_0 == "A"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "hY"
    int_0 = -2333
    dict_0 = {str_0: int_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == "Hy"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "SG"
    int_0 = -2333
    dict_0 = {str_0: int_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == "sg"
    var_1 = module_0.func(*str_0)
    assert var_1 == "s"
#    module_1.object(**var_1)