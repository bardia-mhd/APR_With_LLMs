# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import depth_first_search as module_0
import node as module_1
import builtins as module_2


def test_case_0():
    none_type_0 = None
    var_0 = module_0.depth_first_search(none_type_0, none_type_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "T2jPRn\\G'd ;\x0b"
    none_type_0 = None
    module_0.depth_first_search(str_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    var_0 = module_0.depth_first_search(bool_0, bool_0)
    assert var_0 is True
    node_0 = module_1.Node(incoming_nodes=var_0)
    assert node_0.incoming_nodes is True
    object_0 = module_2.object()
    var_1 = module_0.depth_first_search(node_0, bool_0)
    var_2 = module_0.depth_first_search(object_0, object_0)
    assert var_2 is True
    module_0.depth_first_search(object_0, var_2)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 1233
    node_0 = module_1.Node(int_0, predecessors=int_0)
    node_1 = module_1.Node(predecessors=node_0, incoming_nodes=int_0)
    list_0 = [node_1, node_1, int_0, node_1]
    node_2 = module_1.Node(successors=list_0)
    none_type_0 = None
    var_0 = module_0.depth_first_search(node_1, list_0)
    assert var_0 is False
    module_0.depth_first_search(node_2, none_type_0)