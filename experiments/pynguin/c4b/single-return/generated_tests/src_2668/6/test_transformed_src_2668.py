# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2668 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    str_0 = "10uF"
    var_0 = module_0.func(*str_0)
    assert var_0 == "00"


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "2;`Xy/"
#    module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "1<7#)F"
    bool_0 = True
    tuple_0 = (bool_0, bool_0, bool_0, bool_0)
    tuple_1 = (bool_0, str_0, str_0, tuple_0)
    var_0 = module_0.func(*tuple_1)
    assert var_0 == "1"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "10uF"
    int_0 = 140
    tuple_0 = ()
    tuple_1 = (int_0, str_0, tuple_0)
#    module_0.func(*tuple_1)