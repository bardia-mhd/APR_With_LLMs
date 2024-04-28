# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import depth_first_search as module_0
import node as module_1
import builtins as module_2


def test_case_0():
    int_0 = -113
    var_0 = module_0.depth_first_search(int_0, int_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x05_\xc8\x0eh\xc6^\xa2\xeeg\xd9"
    set_0 = {bytes_0, bytes_0, bytes_0}
    none_type_0 = None
    module_0.depth_first_search(set_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "V\\U|$.qajPn"
    var_0 = module_0.depth_first_search(str_0, str_0)
    assert var_0 is True
    node_0 = module_1.Node(successor=var_0, predecessors=var_0)
    assert node_0.successor is True
    assert node_0.predecessors is True
    var_1 = module_0.depth_first_search(node_0, node_0)
    assert var_1 is True
    var_2 = module_0.depth_first_search(node_0, var_1)
    node_0.predecessors()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "W92'kfzv5Vo"
    var_0 = module_1.Node(
        str_0, successors=str_0, incoming_nodes=str_0, outgoing_nodes=str_0
    )
    node_0 = module_1.Node(successor=var_0, predecessors=var_0)
    var_1 = module_0.depth_first_search(node_0, node_0)
    assert var_1 is True
    var_2 = module_0.depth_first_search(node_0, var_1)
    assert var_2 is False
    module_0.depth_first_search(var_0, var_2)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 1060
    var_0 = module_0.depth_first_search(int_0, int_0)
    assert var_0 is True
    object_0 = module_2.object()
    node_0 = module_1.Node(incoming_nodes=object_0, outgoing_nodes=object_0)
    list_0 = [node_0, node_0]
    var_1 = module_0.depth_first_search(object_0, object_0)
    assert var_1 is True
    var_2 = module_0.depth_first_search(node_0, node_0)
    assert var_2 is True
    node_1 = module_1.Node(
        successor=list_0,
        successors=list_0,
        predecessors=node_0,
        incoming_nodes=object_0,
        outgoing_nodes=node_0,
    )
    var_3 = module_0.depth_first_search(node_1, object_0)
    var_4 = module_0.depth_first_search(node_1, node_1)
    assert var_4 is True
    var_5 = module_0.depth_first_search(object_0, object_0)
    assert var_5 is True
    node_0.successors()