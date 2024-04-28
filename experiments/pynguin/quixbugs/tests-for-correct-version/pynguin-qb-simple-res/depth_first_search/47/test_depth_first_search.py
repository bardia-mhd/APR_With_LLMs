# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import depth_first_search as module_0
import node as module_1


def test_case_0():
    str_0 = " I\\T\t]\\L95X\x0ce]^R@V"
    var_0 = module_0.depth_first_search(str_0, str_0)
    assert var_0 is True


def test_case_1():
    int_0 = -1194
    node_0 = module_1.Node(predecessors=int_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == -1194
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    var_0 = module_0.depth_first_search(node_0, int_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xba"
    node_0 = module_1.Node(successor=bytes_0, successors=bytes_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor == b"\xba"
    assert node_0.successors == b"\xba"
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    var_0 = module_0.depth_first_search(bytes_0, bytes_0)
    assert var_0 is True
    module_0.depth_first_search(node_0, bytes_0)


def test_case_3():
    node_0 = module_1.Node()
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    list_0 = [node_0, node_0, node_0, node_0]
    node_1 = module_1.Node(list_0, list_0, list_0, outgoing_nodes=list_0)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert (
        f"{type(node_1.value).__module__}.{type(node_1.value).__qualname__}"
        == "builtins.list"
    )
    assert len(node_1.value) == 4
    assert (
        f"{type(node_1.successor).__module__}.{type(node_1.successor).__qualname__}"
        == "builtins.list"
    )
    assert len(node_1.successor) == 4
    assert (
        f"{type(node_1.successors).__module__}.{type(node_1.successors).__qualname__}"
        == "builtins.list"
    )
    assert len(node_1.successors) == 4
    assert node_1.predecessors == []
    assert node_1.incoming_nodes == []
    assert (
        f"{type(node_1.outgoing_nodes).__module__}.{type(node_1.outgoing_nodes).__qualname__}"
        == "builtins.list"
    )
    assert len(node_1.outgoing_nodes) == 4
    var_0 = module_0.depth_first_search(node_1, list_0)
    assert var_0 is False