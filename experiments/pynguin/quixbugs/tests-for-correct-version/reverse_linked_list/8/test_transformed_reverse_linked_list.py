# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import reverse_linked_list as module_0
import node as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xb9\xe2E\xe7"
#    module_0.reverse_linked_list(bytes_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.reverse_linked_list(none_type_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    node_0 = module_1.Node()
    var_0 = module_0.reverse_linked_list(node_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value is None
    assert var_0.successor is None
    assert var_0.successors == []
    assert var_0.predecessors == []
    assert var_0.incoming_nodes == []
    assert var_0.outgoing_nodes == []
    var_1 = module_0.reverse_linked_list(var_0)
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "node.Node"
    assert var_1.value is None
    assert var_1.successor is None
    assert var_1.successors == []
    assert var_1.predecessors == []
    assert var_1.incoming_nodes == []
    assert var_1.outgoing_nodes == []
    bytes_0 = b'"\x86\xd4C\xbe\xa4\xf8\x8eh'
#    module_0.reverse_linked_list(bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    set_0 = set()
    list_0 = [set_0, set_0, set_0]
    node_0 = module_1.Node(successor=list_0, successors=list_0, outgoing_nodes=set_0)
#    module_0.reverse_linked_list(node_0)
