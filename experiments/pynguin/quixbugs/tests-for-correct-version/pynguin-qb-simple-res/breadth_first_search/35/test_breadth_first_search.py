# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import breadth_first_search as module_0
import node as module_1
import collections as module_2


def test_case_0():
    bytes_0 = b"\xfb\x8c7\xc4H\xe7\x08\xbe\x0eE\xa5\x15"
    var_0 = module_0.breadth_first_search(bytes_0, bytes_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xce"
    node_0 = module_1.Node(successors=bytes_0, incoming_nodes=bytes_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == b"\xce"
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == b"\xce"
    assert node_0.outgoing_nodes == []
    module_0.breadth_first_search(node_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"WM"
    node_0 = module_1.Node(successor=bytes_0, incoming_nodes=bytes_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor == b"WM"
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == b"WM"
    assert node_0.outgoing_nodes == []
    var_0 = module_0.breadth_first_search(node_0, bytes_0)
    assert var_0 is False
    module_2.deque(**node_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x03\x90\x9fcA\x83\x01\xb3-7\xe9T\xac\xba\x02\xc9s9"
    node_0 = module_1.Node(successors=bytes_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == b"\x03\x90\x9fcA\x83\x01\xb3-7\xe9T\xac\xba\x02\xc9s9"
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    bool_0 = True
    tuple_0 = (node_0, bool_0, bool_0)
    none_type_0 = None
    node_1 = module_1.Node(
        successors=tuple_0, predecessors=none_type_0, outgoing_nodes=none_type_0
    )
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert node_1.value is None
    assert node_1.successor is None
    assert (
        f"{type(node_1.successors).__module__}.{type(node_1.successors).__qualname__}"
        == "builtins.tuple"
    )
    assert len(node_1.successors) == 3
    assert node_1.predecessors is None
    assert node_1.incoming_nodes == []
    assert node_1.outgoing_nodes is None
    var_0 = module_0.breadth_first_search(node_1, bool_0)
    assert var_0 is True
    module_0.breadth_first_search(none_type_0, tuple_0)