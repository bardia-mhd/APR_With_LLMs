# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2446 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "s@IfGW\r76Ya"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "Y$c )hHG"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Q 0T'\n1P@}\\]vhY !d("
    var_0 = module_0.func(*str_0)
    object_0 = module_1.object()
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "9Inwz pG"
    var_0 = module_0.func(*str_0)
    none_type_0 = None
    module_0.func(*none_type_0)