# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1018 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "^4V#3"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "^4V#3"
    var_0 = module_0.func(*str_0)
    module_0.func()


def test_case_3():
    str_0 = "4V3"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "43:Q"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0]
    var_1 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "43:"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0]
    var_1 = module_0.func(*list_0)
    module_1.object(**var_1)