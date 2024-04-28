# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import reverse_linked_list as module_0
import node as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    module_0.reverse_linked_list(bool_0)


def test_case_1():
    set_0 = set()
    var_0 = module_0.reverse_linked_list(set_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    node_0 = module_1.Node(successors=none_type_0, predecessors=none_type_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors is None
    assert node_0.predecessors is None
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    var_0 = module_0.reverse_linked_list(node_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value is None
    assert var_0.successor is None
    assert var_0.successors is None
    assert var_0.predecessors is None
    assert var_0.incoming_nodes == []
    assert var_0.outgoing_nodes == []
    var_0.successor()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    none_type_0 = None
    var_0 = module_0.reverse_linked_list(none_type_0)
    node_0 = module_1.Node(successor=bool_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is True
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    module_0.reverse_linked_list(node_0)