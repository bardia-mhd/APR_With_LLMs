# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1703 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "NOLa0ZgG!`_"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_1():
    str_0 = "NOLa0ZgG!`_"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "tAo<&/FjK3cRhk/}"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "`o<&&/FjXhk//"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "/nk//"
    var_0 = module_0.func(*str_0)
    object_0 = module_1.object()
    var_1 = module_0.func(*var_0)
    object_1 = module_1.object()
    module_0.func()