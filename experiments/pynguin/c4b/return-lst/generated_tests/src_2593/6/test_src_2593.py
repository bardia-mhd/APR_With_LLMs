# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2593 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 109
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 21
    tuple_0 = ()
    list_0 = [int_0, int_0, tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)
    bool_0 = True
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*list_0)
    list_1 = [bool_0, var_1, var_2, var_1]
    var_3 = module_0.func(*list_1)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    int_0 = 3542
    list_1 = [int_0, int_0, int_0]
    var_1 = module_0.func(*list_1)
    module_0.func(*bool_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 28
    tuple_0 = ()
    list_0 = [int_0, int_0, tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_1.object()
    var_1 = module_0.func(*list_0)
    int_0 = 108
    list_1 = [int_0, int_0, int_0]
    var_2 = module_0.func(*list_1)
    module_0.func()