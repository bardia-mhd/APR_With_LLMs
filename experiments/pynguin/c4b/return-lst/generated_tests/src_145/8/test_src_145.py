# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_145 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func(*bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 708
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 685
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 699
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 685
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_1.object()
    var_2 = module_0.func(*var_0)
    object_0 = module_1.object()
    module_0.func()