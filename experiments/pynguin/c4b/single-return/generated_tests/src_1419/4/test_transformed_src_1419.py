# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1419 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    tuple_1 = (tuple_0,)
#    module_0.func(*tuple_1)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "uSJ<H"
    var_0 = module_0.func(*str_0)
    assert var_0 == "U"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "uSJ<H"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Usj<h"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "O?|T3"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "o?|t3"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "uSJz<H"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "uSJz<H"
    var_1 = module_0.func(*str_0)
    assert var_1 == "U"
    object_0 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "VScJ<H"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "VScJ<H"
    var_1 = module_0.func(*str_0)
    assert var_1 == "v"
#    module_0.func()