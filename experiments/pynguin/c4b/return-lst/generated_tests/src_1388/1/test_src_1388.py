# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1388 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -3010
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    str_0 = "[dfo!"
    list_1 = [str_0, str_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()