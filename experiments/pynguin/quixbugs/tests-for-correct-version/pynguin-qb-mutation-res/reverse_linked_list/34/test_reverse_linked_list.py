# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import reverse_linked_list as module_0
import node as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -442
    module_0.reverse_linked_list(int_0)


def test_case_1():
    set_0 = set()
    var_0 = module_0.reverse_linked_list(set_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    set_0 = set()
    var_0 = module_0.reverse_linked_list(set_0)
    list_0 = [var_0]
    node_0 = module_1.Node(list_0, list_0)
    module_0.reverse_linked_list(node_0)


def test_case_3():
    str_0 = "n&c:'\\KRbqo"
    none_type_0 = None
    node_0 = module_1.Node(
        successors=str_0, incoming_nodes=none_type_0, outgoing_nodes=none_type_0
    )
    var_0 = module_0.reverse_linked_list(node_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value is None
    assert var_0.successor is None
    assert var_0.successors == "n&c:'\\KRbqo"
    assert var_0.predecessors == []
    assert var_0.incoming_nodes is None
    assert var_0.outgoing_nodes is None