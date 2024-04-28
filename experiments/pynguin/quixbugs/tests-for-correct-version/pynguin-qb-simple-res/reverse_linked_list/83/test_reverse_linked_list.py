# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import reverse_linked_list as module_0
import node as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\n\xa8\xc6\xa2\x81G\x9eB\x93\x8a\xb4\xbb\xcf\x99au\x9a"
    module_0.reverse_linked_list(bytes_0)


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.reverse_linked_list(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    node_0 = module_1.Node(
        successors=bool_0, predecessors=bool_0, outgoing_nodes=bool_0
    )
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors is True
    assert node_0.predecessors is True
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes is True
    node_1 = module_1.Node(bool_0, successors=bool_0)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert node_1.value is True
    assert node_1.successor is None
    assert node_1.successors is True
    assert node_1.predecessors == []
    assert node_1.incoming_nodes == []
    assert node_1.outgoing_nodes == []
    var_0 = module_0.reverse_linked_list(node_1)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value is True
    assert var_0.successor is None
    assert var_0.successors is True
    assert var_0.predecessors == []
    assert var_0.incoming_nodes == []
    assert var_0.outgoing_nodes == []
    var_1 = module_0.reverse_linked_list(var_0)
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "node.Node"
    assert var_1.value is True
    assert var_1.successor is None
    assert var_1.successors is True
    assert var_1.predecessors == []
    assert var_1.incoming_nodes == []
    assert var_1.outgoing_nodes == []
    list_0 = []
    var_2 = module_0.reverse_linked_list(var_0)
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "node.Node"
    assert var_2.value is True
    assert var_2.successor is None
    assert var_2.successors is True
    assert var_2.predecessors == []
    assert var_2.incoming_nodes == []
    assert var_2.outgoing_nodes == []
    var_3 = module_0.reverse_linked_list(list_0)
    var_1.successor()


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    var_0 = module_0.reverse_linked_list(none_type_0)
    node_0 = module_1.Node(
        successors=var_0, predecessors=none_type_0, outgoing_nodes=none_type_0
    )
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors is None
    assert node_0.predecessors is None
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes is None
    var_1 = module_0.reverse_linked_list(node_0)
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "node.Node"
    assert var_1.value is None
    assert var_1.successor is None
    assert var_1.successors is None
    assert var_1.predecessors is None
    assert var_1.incoming_nodes == []
    assert var_1.outgoing_nodes is None
    none_type_1 = None
    var_2 = module_1.Node(
        var_0, var_1, incoming_nodes=none_type_1, outgoing_nodes=var_0
    )
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "node.Node"
    assert var_2.value is None
    assert (
        f"{type(var_2.successor).__module__}.{type(var_2.successor).__qualname__}"
        == "node.Node"
    )
    assert var_2.successors == []
    assert var_2.predecessors == []
    assert var_2.incoming_nodes is None
    assert var_2.outgoing_nodes is None
    var_3 = module_0.reverse_linked_list(var_2)
    assert (
        f"{type(node_0.successor).__module__}.{type(node_0.successor).__qualname__}"
        == "node.Node"
    )
    assert (
        f"{type(var_1.successor).__module__}.{type(var_1.successor).__qualname__}"
        == "node.Node"
    )
    assert var_2.successor is None
    assert f"{type(var_3).__module__}.{type(var_3).__qualname__}" == "node.Node"
    assert var_3.value is None
    assert (
        f"{type(var_3.successor).__module__}.{type(var_3.successor).__qualname__}"
        == "node.Node"
    )
    assert var_3.successors is None
    assert var_3.predecessors is None
    assert var_3.incoming_nodes == []
    assert var_3.outgoing_nodes is None
    var_4 = module_0.reverse_linked_list(none_type_1)
    var_5 = module_0.reverse_linked_list(var_3)
    assert node_0.successor is None
    assert var_1.successor is None
    assert (
        f"{type(var_2.successor).__module__}.{type(var_2.successor).__qualname__}"
        == "node.Node"
    )
    assert var_3.successor is None
    assert f"{type(var_5).__module__}.{type(var_5).__qualname__}" == "node.Node"
    assert var_5.value is None
    assert (
        f"{type(var_5.successor).__module__}.{type(var_5.successor).__qualname__}"
        == "node.Node"
    )
    assert var_5.successors == []
    assert var_5.predecessors == []
    assert var_5.incoming_nodes is None
    assert var_5.outgoing_nodes is None
    set_0 = set()
    var_6 = module_0.reverse_linked_list(set_0)
    var_7 = module_0.reverse_linked_list(set_0)
    var_8 = module_0.reverse_linked_list(var_6)
    var_9 = module_0.reverse_linked_list(var_4)
    var_10 = module_0.reverse_linked_list(var_0)
    var_7.predecessors()