# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_890 as module_0
import builtins as module_1


def test_case_0():
    float_0 = 1051.3139
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)


def test_case_1():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 1046.26253036045
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
#    module_1.object(*float_0, **var_0)