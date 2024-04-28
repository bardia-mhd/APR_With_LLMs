# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import node as module_0
import topological_ordering as module_1


def test_case_0():
    node_0 = module_0.Node()
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    tuple_0 = (node_0,)
    var_0 = module_1.topological_ordering(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xe8D\x0bL\xa3\xf5\xfc\xe5\x87\x17\xa4\xee\x06i#tB8e\x9b"
    module_1.topological_ordering(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    node_0 = module_0.Node()
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    tuple_0 = (node_0,)
    none_type_0 = None
    node_1 = module_0.Node(predecessors=none_type_0, incoming_nodes=tuple_0)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert node_1.value is None
    assert node_1.successor is None
    assert node_1.successors == []
    assert node_1.predecessors is None
    assert (
        f"{type(node_1.incoming_nodes).__module__}.{type(node_1.incoming_nodes).__qualname__}"
        == "builtins.tuple"
    )
    assert len(node_1.incoming_nodes) == 1
    assert node_1.outgoing_nodes == []
    dict_0 = {node_0: node_1, node_1: node_0, tuple_0: tuple_0, node_0: node_0}
    module_1.topological_ordering(dict_0)


def test_case_3():
    node_0 = module_0.Node()
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    tuple_0 = (node_0,)
    node_1 = module_0.Node(
        successors=tuple_0, predecessors=tuple_0, outgoing_nodes=tuple_0
    )
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert node_1.value is None
    assert node_1.successor is None
    assert (
        f"{type(node_1.successors).__module__}.{type(node_1.successors).__qualname__}"
        == "builtins.tuple"
    )
    assert len(node_1.successors) == 1
    assert (
        f"{type(node_1.predecessors).__module__}.{type(node_1.predecessors).__qualname__}"
        == "builtins.tuple"
    )
    assert len(node_1.predecessors) == 1
    assert node_1.incoming_nodes == []
    assert (
        f"{type(node_1.outgoing_nodes).__module__}.{type(node_1.outgoing_nodes).__qualname__}"
        == "builtins.tuple"
    )
    assert len(node_1.outgoing_nodes) == 1
    list_0 = [node_0, node_1]
    var_0 = module_1.topological_ordering(list_0)


def test_case_4():
    node_0 = module_0.Node()
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    tuple_0 = (node_0,)
    node_1 = module_0.Node(
        successors=tuple_0, predecessors=tuple_0, outgoing_nodes=tuple_0
    )
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert node_1.value is None
    assert node_1.successor is None
    assert (
        f"{type(node_1.successors).__module__}.{type(node_1.successors).__qualname__}"
        == "builtins.tuple"
    )
    assert len(node_1.successors) == 1
    assert (
        f"{type(node_1.predecessors).__module__}.{type(node_1.predecessors).__qualname__}"
        == "builtins.tuple"
    )
    assert len(node_1.predecessors) == 1
    assert node_1.incoming_nodes == []
    assert (
        f"{type(node_1.outgoing_nodes).__module__}.{type(node_1.outgoing_nodes).__qualname__}"
        == "builtins.tuple"
    )
    assert len(node_1.outgoing_nodes) == 1
    list_0 = [node_1, node_1, node_1]
    var_0 = module_1.topological_ordering(list_0)