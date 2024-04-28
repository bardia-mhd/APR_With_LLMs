# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import detect_cycle as module_0
import node as module_1


def test_case_0():
    none_type_0 = None
    var_0 = module_0.detect_cycle(none_type_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    module_0.detect_cycle(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -5608.4722
    node_0 = module_1.Node(float_0, incoming_nodes=float_0, outgoing_nodes=float_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value == pytest.approx(-5608.4722, abs=0.01, rel=0.01)
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == pytest.approx(-5608.4722, abs=0.01, rel=0.01)
    assert node_0.outgoing_nodes == pytest.approx(-5608.4722, abs=0.01, rel=0.01)
    var_0 = module_0.detect_cycle(node_0)
    assert var_0 is False
    node_0.successors()


def test_case_3():
    none_type_0 = None
    node_0 = module_1.Node(
        successor=none_type_0, predecessors=none_type_0, outgoing_nodes=none_type_0
    )
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors is None
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes is None
    node_1 = module_1.Node(
        successor=node_0,
        predecessors=none_type_0,
        incoming_nodes=none_type_0,
        outgoing_nodes=node_0,
    )
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert node_1.value is None
    assert (
        f"{type(node_1.successor).__module__}.{type(node_1.successor).__qualname__}"
        == "node.Node"
    )
    assert node_1.successors == []
    assert node_1.predecessors is None
    assert node_1.incoming_nodes is None
    assert (
        f"{type(node_1.outgoing_nodes).__module__}.{type(node_1.outgoing_nodes).__qualname__}"
        == "node.Node"
    )
    var_0 = module_0.detect_cycle(node_1)
    assert var_0 is False