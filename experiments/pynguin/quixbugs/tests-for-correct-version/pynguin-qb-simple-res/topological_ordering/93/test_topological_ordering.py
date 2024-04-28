# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import topological_ordering as module_0
import node as module_1


def test_case_0():
    list_0 = []
    var_0 = module_0.topological_ordering(list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"k(9\xd0\xdd\x18hzr\xa4\x0b0\xa6\x8d\x19"
    module_0.topological_ordering(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    node_0 = module_1.Node()
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    module_0.topological_ordering(node_0)


def test_case_3():
    node_0 = module_1.Node()
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    list_0 = [node_0, node_0]
    var_0 = module_0.topological_ordering(list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"y\xb2Z\x05\xd4h\x04?"
    list_0 = [bytes_0]
    node_0 = module_1.Node(successor=list_0, successors=list_0, outgoing_nodes=list_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor == [b"y\xb2Z\x05\xd4h\x04?"]
    assert node_0.successors == [b"y\xb2Z\x05\xd4h\x04?"]
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == [b"y\xb2Z\x05\xd4h\x04?"]
    dict_0 = {node_0: node_0}
    module_0.topological_ordering(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "Ma35TFBAG"
    node_0 = module_1.Node(successor=str_0, successors=str_0, incoming_nodes=str_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor == "Ma35TFBAG"
    assert node_0.successors == "Ma35TFBAG"
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == "Ma35TFBAG"
    assert node_0.outgoing_nodes == []
    none_type_0 = None
    node_1 = module_1.Node(
        successor=none_type_0, predecessors=node_0, outgoing_nodes=node_0
    )
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert node_1.value is None
    assert node_1.successor is None
    assert node_1.successors == []
    assert (
        f"{type(node_1.predecessors).__module__}.{type(node_1.predecessors).__qualname__}"
        == "node.Node"
    )
    assert node_1.incoming_nodes == []
    assert (
        f"{type(node_1.outgoing_nodes).__module__}.{type(node_1.outgoing_nodes).__qualname__}"
        == "node.Node"
    )
    list_0 = [node_0, node_1, node_1, node_0]
    module_0.topological_ordering(list_0)


def test_case_6():
    node_0 = module_1.Node()
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    list_0 = [
        node_0,
        node_0,
        node_0,
        node_0,
        node_0,
        node_0,
        node_0,
        node_0,
        node_0,
        node_0,
        node_0,
        node_0,
        node_0,
        node_0,
        node_0,
        node_0,
        node_0,
        node_0,
        node_0,
        node_0,
        node_0,
        node_0,
        node_0,
        node_0,
        node_0,
    ]
    node_1 = module_1.Node(list_0, outgoing_nodes=list_0)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert (
        f"{type(node_1.value).__module__}.{type(node_1.value).__qualname__}"
        == "builtins.list"
    )
    assert len(node_1.value) == 25
    assert node_1.successor is None
    assert node_1.successors == []
    assert node_1.predecessors == []
    assert node_1.incoming_nodes == []
    assert (
        f"{type(node_1.outgoing_nodes).__module__}.{type(node_1.outgoing_nodes).__qualname__}"
        == "builtins.list"
    )
    assert len(node_1.outgoing_nodes) == 25
    dict_0 = {node_1: list_0}
    var_0 = module_0.topological_ordering(dict_0)