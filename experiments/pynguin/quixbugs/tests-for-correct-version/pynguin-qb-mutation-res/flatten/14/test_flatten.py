# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import flatten as module_0
import builtins as module_1


def test_case_0():
    none_type_0 = None
    var_0 = module_0.flatten(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "_nz-0?8s0pb,1"
    var_0 = module_0.flatten(str_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = '{-a[A/X"Y9\tt#Qt2VE5:'
    list_0 = [str_0, str_0, str_0, str_0]
    tuple_0 = (str_0, list_0)
    var_0 = module_0.flatten(tuple_0)
    module_1.object(*var_0)