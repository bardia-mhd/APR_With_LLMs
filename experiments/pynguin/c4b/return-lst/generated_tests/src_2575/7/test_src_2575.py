# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2575 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = 'd2f]]/"LfuH8'
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "* \r8SBv4/`NVVW"
    bool_0 = True
    list_0 = [str_0, str_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    module_1.object(*var_0)


def test_case_3():
    str_0 = "XBKK}K}`&Oqw,\x0c!9zs"
    set_0 = {str_0, str_0, str_0, str_0, str_0, str_0}
    var_0 = module_0.func(*set_0)