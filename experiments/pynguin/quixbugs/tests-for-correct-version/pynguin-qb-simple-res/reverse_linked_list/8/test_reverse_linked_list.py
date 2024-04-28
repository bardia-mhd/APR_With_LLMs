# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import reverse_linked_list as module_0
import node as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = 'b?mkOlK/$jv"O\t'
    module_0.reverse_linked_list(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    var_0 = module_0.reverse_linked_list(none_type_0)
    bool_0 = True
    module_0.reverse_linked_list(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    node_0 = module_1.Node(successors=none_type_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors is None
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    var_0 = module_0.reverse_linked_list(none_type_0)
    var_1 = module_0.reverse_linked_list(var_0)
    var_2 = module_0.reverse_linked_list(node_0)
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "node.Node"
    assert var_2.value is None
    assert var_2.successor is None
    assert var_2.successors is None
    assert var_2.predecessors == []
    assert var_2.incoming_nodes == []
    assert var_2.outgoing_nodes == []
    var_0.successors()


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    bool_0 = True
    node_0 = module_1.Node(none_type_0, bool_0, outgoing_nodes=bool_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is True
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes is True
    module_0.reverse_linked_list(node_0)