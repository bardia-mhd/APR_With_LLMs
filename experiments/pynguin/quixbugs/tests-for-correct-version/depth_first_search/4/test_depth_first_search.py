# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import depth_first_search as module_0
import node as module_1
import builtins as module_2


def test_case_0():
    none_type_0 = None
    var_0 = module_0.depth_first_search(none_type_0, none_type_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "l4bK*n%[0yQ4U~+%\\3"
    none_type_0 = None
    module_0.depth_first_search(str_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 1161.4453
    var_0 = module_0.depth_first_search(float_0, float_0)
    assert var_0 is True
    str_0 = ")xx~1/s\\\rJ^QP"
    node_0 = module_1.Node(successors=str_0, incoming_nodes=str_0)
    module_0.depth_first_search(node_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    var_0 = module_1.Node(bool_0, outgoing_nodes=bool_0)
    bool_1 = False
    tuple_0 = (bool_1, var_0)
    var_1 = module_0.depth_first_search(var_0, tuple_0)
    assert var_1 is False
    module_2.object(**tuple_0)