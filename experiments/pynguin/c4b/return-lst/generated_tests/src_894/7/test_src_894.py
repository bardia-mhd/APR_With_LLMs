# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_894 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "rzZ \n!a/e"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = '?A]@iN\tGD"Ax!!2'
    var_0 = module_0.func(*str_0)
    module_0.func()


def test_case_3():
    str_0 = "rzZ \n!a/e"
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ";a* n@Tz'Hff|1ldAo"
    var_0 = module_0.func(*str_0)
    none_type_0 = None
    list_0 = [str_0, var_0, none_type_0]
    var_1 = module_0.func(*list_0)
    object_0 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "cC?"
    var_0 = module_0.func(*str_0)
    list_0 = []
    list_1 = [str_0, list_0, list_0]
    var_1 = module_0.func(*list_1)
    module_0.func()