# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import reverse_linked_list as module_0
import node as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    module_0.reverse_linked_list(bool_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.reverse_linked_list(none_type_0)
    var_1 = module_0.reverse_linked_list(var_0)


def test_case_2():
    none_type_0 = None
    var_0 = module_0.reverse_linked_list(none_type_0)
    node_0 = module_1.Node(incoming_nodes=var_0)
    var_1 = module_0.reverse_linked_list(node_0)
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "node.Node"
    assert var_1.value is None
    assert var_1.successor is None
    assert var_1.successors == []
    assert var_1.predecessors == []
    assert var_1.incoming_nodes is None
    assert var_1.outgoing_nodes == []


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    node_0 = module_1.Node(successor=none_type_0)
    str_0 = '""kDo&Y\x0cv \x0c'
    bool_0 = True
    var_0 = module_0.reverse_linked_list(none_type_0)
    node_1 = module_1.Node(node_0, str_0, incoming_nodes=bool_0)
    module_0.reverse_linked_list(node_1)