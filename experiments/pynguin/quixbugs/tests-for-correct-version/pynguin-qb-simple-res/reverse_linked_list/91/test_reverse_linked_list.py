# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import reverse_linked_list as module_0
import node as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "a$\\2L'_fgFF"
    module_0.reverse_linked_list(str_0)


def test_case_1():
    bool_0 = False
    var_0 = module_0.reverse_linked_list(bool_0)
    none_type_0 = None
    var_1 = module_0.reverse_linked_list(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    node_0 = module_1.Node()
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    var_0 = module_0.reverse_linked_list(node_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value is None
    assert var_0.successor is None
    assert var_0.successors == []
    assert var_0.predecessors == []
    assert var_0.incoming_nodes == []
    assert var_0.outgoing_nodes == []
    dict_0 = {}
    var_1 = module_0.reverse_linked_list(var_0)
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "node.Node"
    assert var_1.value is None
    assert var_1.successor is None
    assert var_1.successors == []
    assert var_1.predecessors == []
    assert var_1.incoming_nodes == []
    assert var_1.outgoing_nodes == []
    var_2 = module_0.reverse_linked_list(var_0)
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "node.Node"
    assert var_2.value is None
    assert var_2.successor is None
    assert var_2.successors == []
    assert var_2.predecessors == []
    assert var_2.incoming_nodes == []
    assert var_2.outgoing_nodes == []
    var_3 = module_0.reverse_linked_list(var_1)
    assert f"{type(var_3).__module__}.{type(var_3).__qualname__}" == "node.Node"
    assert var_3.value is None
    assert var_3.successor is None
    assert var_3.successors == []
    assert var_3.predecessors == []
    assert var_3.incoming_nodes == []
    assert var_3.outgoing_nodes == []
    var_4 = module_0.reverse_linked_list(dict_0)
    var_5 = module_0.reverse_linked_list(var_0)
    assert f"{type(var_5).__module__}.{type(var_5).__qualname__}" == "node.Node"
    assert var_5.value is None
    assert var_5.successor is None
    assert var_5.successors == []
    assert var_5.predecessors == []
    assert var_5.incoming_nodes == []
    assert var_5.outgoing_nodes == []
    node_0.successors()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"$\x03%\x18\xc9{%\x83\n\xe2d\x1ba\xb5\xab\xd0"
    node_0 = module_1.Node()
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    node_1 = module_1.Node(bytes_0, bytes_0, bytes_0, bytes_0, outgoing_nodes=node_0)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert node_1.value == b"$\x03%\x18\xc9{%\x83\n\xe2d\x1ba\xb5\xab\xd0"
    assert node_1.successor == b"$\x03%\x18\xc9{%\x83\n\xe2d\x1ba\xb5\xab\xd0"
    assert node_1.successors == b"$\x03%\x18\xc9{%\x83\n\xe2d\x1ba\xb5\xab\xd0"
    assert node_1.predecessors == b"$\x03%\x18\xc9{%\x83\n\xe2d\x1ba\xb5\xab\xd0"
    assert node_1.incoming_nodes == []
    assert (
        f"{type(node_1.outgoing_nodes).__module__}.{type(node_1.outgoing_nodes).__qualname__}"
        == "node.Node"
    )
    module_0.reverse_linked_list(node_1)