# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1419 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    dict_0 = {}
    list_0 = [dict_0, dict_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "WJzbq)<twS>hfM%i9"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "WJzbq)<twS>hfM%i9"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "O M"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "om"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "\tV}J"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "v}j"
    var_1 = module_0.func(*list_0)
    assert var_1 == "v}j"
    var_2 = module_0.func(*var_0)
    assert var_2 == "V"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "-p"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "-p"
    var_1 = module_0.func(*var_0)
    assert var_1 == "-"
    var_2 = module_0.func(*list_0)
    assert var_2 == "-p"
    object_0 = module_1.object()
    var_3 = module_0.func(*var_1)
    assert var_3 == "-"
    module_0.func()