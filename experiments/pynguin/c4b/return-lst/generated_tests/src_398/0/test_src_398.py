# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_398 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "7"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "5"
    var_0 = module_0.func(*str_0)
    var_1 = module_1.object()
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "4"
    var_0 = module_0.func(*str_0)
    module_0.func()


def test_case_4():
    str_0 = "77"
    object_0 = module_1.object()
    int_0 = 1514
    list_0 = [str_0, object_0, str_0, int_0]
    var_0 = module_0.func(*list_0)