# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import reverse_linked_list as module_0
import node as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -2218
    module_0.reverse_linked_list(int_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.reverse_linked_list(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    tuple_0 = ()
    node_0 = module_1.Node(tuple_0, tuple_0, outgoing_nodes=tuple_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value == ()
    assert node_0.successor == ()
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == ()
    node_1 = module_1.Node(tuple_0, successors=node_0, incoming_nodes=node_0)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert node_1.value == ()
    assert node_1.successor is None
    assert (
        f"{type(node_1.successors).__module__}.{type(node_1.successors).__qualname__}"
        == "node.Node"
    )
    assert node_1.predecessors == []
    assert (
        f"{type(node_1.incoming_nodes).__module__}.{type(node_1.incoming_nodes).__qualname__}"
        == "node.Node"
    )
    assert node_1.outgoing_nodes == []
    var_0 = module_0.reverse_linked_list(node_1)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value == ()
    assert var_0.successor is None
    assert (
        f"{type(var_0.successors).__module__}.{type(var_0.successors).__qualname__}"
        == "node.Node"
    )
    assert var_0.predecessors == []
    assert (
        f"{type(var_0.incoming_nodes).__module__}.{type(var_0.incoming_nodes).__qualname__}"
        == "node.Node"
    )
    assert var_0.outgoing_nodes == []
    node_1.successors()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 2584
    node_0 = module_1.Node(successor=int_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor == 2584
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    module_0.reverse_linked_list(node_0)