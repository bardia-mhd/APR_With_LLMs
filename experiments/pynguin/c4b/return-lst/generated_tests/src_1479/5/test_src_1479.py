# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1479 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "s\x0cH\n"
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*var_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "s\x0cH\n"
    var_0 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "?n>[\x0b4H"
    str_1 = "-DY43%gUw.3\n3v`~<i"
    var_0 = module_0.func(*str_0)
    str_2 = " -hLl}Oz+"
    dict_0 = {str_0: str_0, str_1: str_1, str_2: str_0}
    module_1.object(**dict_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "s\x0cH\n"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "s\x0cH\n"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    var_2 = module_0.func(*var_0)
    module_0.func()