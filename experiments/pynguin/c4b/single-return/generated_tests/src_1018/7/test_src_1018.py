# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1018 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "2B0T"
    var_0 = module_0.func(*str_0)
    assert var_0 == 2
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "Kr0g9"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 2151
    object_0 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "2B0T"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 479
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "20T"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 129
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "29mB0T"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 2711
    var_1 = module_0.func(*str_0)
    assert var_1 == 2
    module_1.object(*var_1, **var_1)