# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1571 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "[U"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "[u"
    var_1 = module_0.func(*var_0)
    assert var_1 == "["
    var_2 = module_0.func(*var_1)
    assert var_2 == "["
    var_3 = module_0.func(*var_2)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "j{m{_wfw"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "j{m{_wfw"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "[e"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "[e"
    var_1 = module_0.func(*var_0)
    assert var_1 == "["
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ""
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    list_0 = [var_0, var_0, var_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "s[U"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "S[u"
    list_0 = [var_0, var_0, var_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == "S[u"
    var_2 = module_0.func(*list_0)
    assert var_2 == "S[u"
    module_0.func()