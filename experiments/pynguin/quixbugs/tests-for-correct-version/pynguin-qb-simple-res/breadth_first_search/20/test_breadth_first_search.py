# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import breadth_first_search as module_0
import node as module_1


def test_case_0():
    str_0 = "n\x0b="
    var_0 = module_0.breadth_first_search(str_0, str_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = 1970.815016
    none_type_0 = None
    module_0.breadth_first_search(float_0, none_type_0)


def test_case_2():
    bool_0 = False
    node_0 = module_1.Node(successor=bool_0, predecessors=bool_0, incoming_nodes=bool_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is False
    assert node_0.successors == []
    assert node_0.predecessors is False
    assert node_0.incoming_nodes is False
    assert node_0.outgoing_nodes == []
    var_0 = module_0.breadth_first_search(node_0, bool_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "]iliI\x0bt4cy&\x0bB"
    node_0 = module_1.Node(successors=str_0, predecessors=str_0, outgoing_nodes=str_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == "]iliI\x0bt4cy&\x0bB"
    assert node_0.predecessors == "]iliI\x0bt4cy&\x0bB"
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == "]iliI\x0bt4cy&\x0bB"
    module_0.breadth_first_search(node_0, str_0)