# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import reverse_linked_list as module_0
import node as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b'\xbb\xfe%\x8cf\xce\xc2\xf8\xdb\xa2\xd6}.\xaa\xf9"\xee\x03'
    module_0.reverse_linked_list(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    var_0 = module_0.reverse_linked_list(bool_0)
    bytes_0 = b'\xbb\xfe%\x8cf\xce\xc2\xf8\xdb\xa2\xd6}.\xaa\xf9"\xee\x03'
    module_0.reverse_linked_list(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 934
    bool_0 = False
    var_0 = module_1.Node(successor=bool_0, predecessors=int_0, outgoing_nodes=int_0)
    var_1 = module_0.reverse_linked_list(var_0)
    assert var_0.successor is None
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "node.Node"
    assert var_1.value is None
    assert var_1.successor is None
    assert var_1.successors == []
    assert var_1.predecessors == 934
    assert var_1.incoming_nodes == []
    assert var_1.outgoing_nodes == 934
    module_0.reverse_linked_list(int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xb8\x07\xbe"
    none_type_0 = None
    node_0 = module_1.Node(none_type_0, bytes_0, none_type_0)
    module_0.reverse_linked_list(node_0)