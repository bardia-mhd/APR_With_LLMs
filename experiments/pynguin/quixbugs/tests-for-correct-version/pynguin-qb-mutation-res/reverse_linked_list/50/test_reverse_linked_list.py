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


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    node_0 = module_1.Node(outgoing_nodes=bool_0)
    var_0 = module_0.reverse_linked_list(node_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value is None
    assert var_0.successor is None
    assert var_0.successors == []
    assert var_0.predecessors == []
    assert var_0.incoming_nodes == []
    assert var_0.outgoing_nodes is False
    bool_1 = True
    module_0.reverse_linked_list(bool_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "3`h3k1ee"
    none_type_0 = None
    node_0 = module_1.Node(
        successor=str_0, successors=str_0, outgoing_nodes=none_type_0
    )
    module_0.reverse_linked_list(node_0)