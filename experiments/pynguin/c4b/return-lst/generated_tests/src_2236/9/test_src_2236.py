# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2236 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    bytes_0 = b"6"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "6"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    str_1 = "8%<UC+GTG_O<Lh"
    var_1 = module_0.func(*str_1)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "4"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_1.object()
    module_0.func()