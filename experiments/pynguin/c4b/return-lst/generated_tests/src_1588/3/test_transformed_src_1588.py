# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1588 as module_0
import builtins as module_1


def test_case_0():
    float_0 = -1154.2
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)


def test_case_1():
    float_0 = -1145.9692077829964
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 721.5
    list_0 = [float_0, float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_1.object()
    var_1 = module_0.func(*var_0)
    object_1 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 721.5
    list_0 = [float_0, float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    float_0 = 715.3425130636876
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()