# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_463 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "7Tq(d.M\t8TdBgU\x0bu"
    var_0 = module_0.func(*str_0)
    assert var_0 == "7"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "WO @J.tI+,RW;JrG?r["
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "WO @J.tI+,RW;JrG?r["
    int_0 = 2048
    set_0 = {int_0}
#    module_0.func(*set_0)


def test_case_3():
    str_0 = "WO @J.t9\\,Rj;JrGXr["
    var_0 = module_0.func(*str_0)
    assert var_0 == "w"
    var_1 = module_0.func(*var_0)
    assert var_1 == "W"


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "p'D"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "P'd"
    object_0 = module_1.object()
    var_1 = module_0.func(*var_0)
    assert var_1 == "p"
    var_2 = module_0.func(*var_1)
    assert var_2 == "P"
#    module_0.func()