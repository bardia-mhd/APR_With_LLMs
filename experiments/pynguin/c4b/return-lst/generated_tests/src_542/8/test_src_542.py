# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_542 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "2"
    var_0 = module_0.func(*str_0)
    module_0.func()


def test_case_1():
    int_0 = -218
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    set_0 = set()
    list_1 = [set_0]
    var_1 = module_0.func(*list_1)
    var_2 = module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()