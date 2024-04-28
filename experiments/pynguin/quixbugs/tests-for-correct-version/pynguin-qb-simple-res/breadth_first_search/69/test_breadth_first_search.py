# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import breadth_first_search as module_0
import node as module_1


def test_case_0():
    complex_0 = -234.5413 + 1809j
    var_0 = module_0.breadth_first_search(complex_0, complex_0)
    assert var_0 is True


def test_case_1():
    bool_0 = False
    node_0 = module_1.Node(predecessors=bool_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors is False
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    var_0 = module_0.breadth_first_search(node_0, bool_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    none_type_0 = None
    module_0.breadth_first_search(bool_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b";"
    node_0 = module_1.Node(successors=bytes_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == b";"
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    module_0.breadth_first_search(node_0, bytes_0)