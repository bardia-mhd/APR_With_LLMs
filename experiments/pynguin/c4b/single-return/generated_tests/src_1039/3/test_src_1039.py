# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1039 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "27"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 6
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "32]"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 118
    object_0 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "37]"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 143
    object_0 = module_1.object()
    module_1.object(*list_0)