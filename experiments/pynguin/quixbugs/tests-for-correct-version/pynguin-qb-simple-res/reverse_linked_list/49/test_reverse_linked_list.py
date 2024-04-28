# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import node as module_0
import reverse_linked_list as module_1


def test_case_0():
    float_0 = -785.5505
    node_0 = module_0.Node(float_0, successors=float_0, outgoing_nodes=float_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value == pytest.approx(-785.5505, abs=0.01, rel=0.01)
    assert node_0.successor is None
    assert node_0.successors == pytest.approx(-785.5505, abs=0.01, rel=0.01)
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == pytest.approx(-785.5505, abs=0.01, rel=0.01)
    var_0 = module_1.reverse_linked_list(node_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value == pytest.approx(-785.5505, abs=0.01, rel=0.01)
    assert var_0.successor is None
    assert var_0.successors == pytest.approx(-785.5505, abs=0.01, rel=0.01)
    assert var_0.predecessors == []
    assert var_0.incoming_nodes == []
    assert var_0.outgoing_nodes == pytest.approx(-785.5505, abs=0.01, rel=0.01)


def test_case_1():
    none_type_0 = None
    var_0 = module_1.reverse_linked_list(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    set_0 = {bool_0, bool_0, bool_0}
    node_0 = module_0.Node(successors=set_0, predecessors=set_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == {False}
    assert node_0.predecessors == {False}
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    var_0 = module_1.reverse_linked_list(node_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value is None
    assert var_0.successor is None
    assert var_0.successors == {False}
    assert var_0.predecessors == {False}
    assert var_0.incoming_nodes == []
    assert var_0.outgoing_nodes == []
    none_type_0 = None
    var_1 = module_1.reverse_linked_list(none_type_0)
    node_1 = module_0.Node(set_0, set_0)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert node_1.value == {False}
    assert node_1.successor == {False}
    assert node_1.successors == []
    assert node_1.predecessors == []
    assert node_1.incoming_nodes == []
    assert node_1.outgoing_nodes == []
    var_2 = module_1.reverse_linked_list(var_1)
    module_1.reverse_linked_list(node_1)