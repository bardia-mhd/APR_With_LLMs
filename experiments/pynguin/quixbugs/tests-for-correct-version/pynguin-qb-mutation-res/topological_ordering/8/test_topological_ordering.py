# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import topological_ordering as module_0
import node as module_1


def test_case_0():
    set_0 = set()
    var_0 = module_0.topological_ordering(set_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ",O2#yu[Y}L\nry>W/c"
    set_0 = {str_0, str_0, str_0}
    module_0.topological_ordering(set_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.topological_ordering(none_type_0)


def test_case_3():
    node_0 = module_1.Node()
    list_0 = [node_0]
    var_0 = module_0.topological_ordering(list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    set_0 = set()
    node_0 = module_1.Node(set_0, incoming_nodes=set_0, outgoing_nodes=set_0)
    node_1 = module_1.Node(incoming_nodes=node_0)
    list_0 = [node_1, node_1, node_0]
    var_0 = module_0.topological_ordering(list_0)
    str_0 = "d)6I\\"
    module_0.topological_ordering(str_0)


def test_case_5():
    set_0 = set()
    node_0 = module_1.Node(set_0, incoming_nodes=set_0, outgoing_nodes=set_0)
    list_0 = [node_0, node_0, node_0]
    node_1 = module_1.Node(outgoing_nodes=list_0)
    dict_0 = {node_1: node_0, node_1: node_0}
    var_0 = module_0.topological_ordering(dict_0)