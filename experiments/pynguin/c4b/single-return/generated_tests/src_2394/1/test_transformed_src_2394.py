# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2394 as module_0


def test_case_0():
    str_0 = " ,<<\x0c\\b'"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "`|`;nTG3OjVEA+-nO]0'"
    bool_0 = False
    list_0 = [
        bool_0,
        str_0,
        str_0,
        bool_0,
        bool_0,
        bool_0,
        bool_0,
        bool_0,
        bool_0,
        bool_0,
        str_0,
        bool_0,
    ]
    tuple_0 = (list_0, list_0, bool_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "YES"
#    module_0.func()