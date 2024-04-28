# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import breadth_first_search as module_0
import node as module_1


def test_case_0():
    none_type_0 = None
    var_0 = module_0.breadth_first_search(none_type_0, none_type_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x15\x1f\xa7}\xc7\r\x05k\xc5\x8c`\xd8d\xb7\xc8UX"
    node_0 = module_1.Node(successors=bytes_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == b"\x15\x1f\xa7}\xc7\r\x05k\xc5\x8c`\xd8d\xb7\xc8UX"
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    module_0.breadth_first_search(node_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -363.2
    tuple_0 = (float_0,)
    module_0.breadth_first_search(tuple_0, float_0)


def test_case_3():
    none_type_0 = None
    var_0 = module_0.breadth_first_search(none_type_0, none_type_0)
    assert var_0 is True
    node_0 = module_1.Node(predecessors=var_0, outgoing_nodes=var_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors is True
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes is True
    var_1 = module_0.breadth_first_search(node_0, var_0)
    assert var_1 is False


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xfc"
    node_0 = module_1.Node(bytes_0, bytes_0, bytes_0, incoming_nodes=bytes_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value == b"\xfc"
    assert node_0.successor == b"\xfc"
    assert node_0.successors == b"\xfc"
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == b"\xfc"
    assert node_0.outgoing_nodes == []
    list_0 = [node_0, node_0, bytes_0, bytes_0, node_0]
    node_1 = module_1.Node(bytes_0, successors=list_0)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert node_1.value == b"\xfc"
    assert node_1.successor is None
    assert (
        f"{type(node_1.successors).__module__}.{type(node_1.successors).__qualname__}"
        == "builtins.list"
    )
    assert len(node_1.successors) == 5
    assert node_1.predecessors == []
    assert node_1.incoming_nodes == []
    assert node_1.outgoing_nodes == []
    none_type_0 = None
    module_0.breadth_first_search(node_1, none_type_0)