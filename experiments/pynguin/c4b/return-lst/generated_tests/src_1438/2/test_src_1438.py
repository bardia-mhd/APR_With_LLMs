# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1438 as module_0
import builtins as module_1


def test_case_0():
    str_0 = 'Sw\n/"RDZ:;'
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = 'Sw\n/"RDZ:;'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = 'w\n/"RDZ:;'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    module_1.object(**var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = 'Sw\n/" RDZ:;'
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = 'wf/"DZ:;'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "G f3}7G/\n$T\\$?"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    module_1.object(**var_0)