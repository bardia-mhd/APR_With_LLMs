# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import reverse_linked_list as module_0
import node as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
#    module_0.reverse_linked_list(bool_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.reverse_linked_list(none_type_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    tuple_0 = ()
    node_0 = module_1.Node(tuple_0, tuple_0)
    var_0 = module_0.reverse_linked_list(node_0)
    assert node_0.successor is None
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value == ()
    assert var_0.successor is None
    assert var_0.successors == []
    assert var_0.predecessors == []
    assert var_0.incoming_nodes == []
    assert var_0.outgoing_nodes == []
    float_0 = 1932.2885
#    module_0.reverse_linked_list(float_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    tuple_0 = ()
    node_0 = module_1.Node(tuple_0, tuple_0)
    var_0 = module_0.reverse_linked_list(node_0)
    assert node_0.successor is None
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value == ()
    assert var_0.successor is None
    assert var_0.successors == []
    assert var_0.predecessors == []
    assert var_0.incoming_nodes == []
    assert var_0.outgoing_nodes == []
    float_0 = 1932.2885
    node_1 = module_1.Node(successor=float_0)
#    module_0.reverse_linked_list(node_1)
