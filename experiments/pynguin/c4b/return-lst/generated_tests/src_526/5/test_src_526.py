# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import src_526 as module_1


def test_case_0():
    object_0 = module_0.object()
    set_0 = {object_0, object_0}
    tuple_0 = (set_0,)
    var_0 = module_1.func(*tuple_0)
    var_1 = module_1.func(*var_0)
    var_2 = module_1.func(*tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    list_0 = [set_0, set_0, set_0, set_0]
    var_0 = module_1.func(*list_0)
    module_1.func()


def test_case_2():
    pass


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Q\tIP*:v`}.0\t$'\x0cW|"
    int_0 = -752
    list_0 = [str_0, int_0, str_0, str_0]
    var_0 = module_1.func(*list_0)
    var_1 = module_1.func(*str_0)
    int_1 = -132
    module_1.func(*int_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "H\nQ7"
    none_type_0 = None
    list_0 = [str_0, none_type_0, none_type_0, none_type_0]
    var_0 = module_1.func(*list_0)
    var_1 = module_1.func(*list_0)
    module_1.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "'{VdpM92T BZin:"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_1.func(*list_0)
    module_1.func()