# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1422 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    str_0 = "CZ[7fYeu!b"
    list_0 = [bool_0, bool_0, bool_0, str_0]
    module_0.func(*list_0)


def test_case_1():
    int_0 = 4
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


def test_case_3():
    int_0 = 309
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 274
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 2
    list_0 = [int_0, int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


def test_case_6():
    int_0 = 6
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_1.object()
    object_0 = module_1.object()


@pytest.mark.xfail(strict=True)
def test_case_7():
    int_0 = 5
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_8():
    int_0 = 7
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_9():
    int_0 = 3
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()