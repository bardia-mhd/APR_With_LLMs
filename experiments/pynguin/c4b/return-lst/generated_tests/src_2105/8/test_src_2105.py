# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2105 as module_0


def test_case_0():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 2183
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 502
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    str_0 = "B@@b\nQt>5aN,Jk?='\tZk"
    dict_0 = {int_0: int_0, str_0: str_0, str_0: int_0}
    var_1 = module_0.func(*dict_0)
    module_0.func()