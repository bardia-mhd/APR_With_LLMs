# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_paths as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b""
    var_0 = module_0.shortest_paths(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b""
    var_0 = module_0.shortest_paths(bytes_0, bytes_0)
    module_0.shortest_paths(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    tuple_0 = ()
    str_0 = "F+"
    var_0 = module_0.shortest_paths(str_0, tuple_0)
    module_0.shortest_paths(tuple_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    tuple_0 = ()
    str_0 = "++"
    var_0 = module_0.shortest_paths(str_0, tuple_0)
    var_1 = module_0.shortest_paths(str_0, var_0)
    object_0 = module_1.object()
    module_0.shortest_paths(var_0, var_1)