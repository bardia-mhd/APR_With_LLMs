# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2035 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "hG[(^OZ?"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


def test_case_2():
    str_0 = "$t"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
    list_0 = [str_0, str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 1


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "KV"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    str_1 = ">Tn"
    var_1 = module_0.func(*str_1)
    assert var_1 == 0
    list_1 = [str_1, str_1]
    var_2 = module_0.func(*list_1)
    assert var_2 == 1
    module_1.object(*str_1)