# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import depth_first_search as module_0
import node as module_1


def test_case_0():
    bool_0 = True
    var_0 = module_0.depth_first_search(bool_0, bool_0)
    assert var_0 is True


def test_case_1():
    list_0 = []
    node_0 = module_1.Node(successor=list_0, predecessors=list_0)
    var_0 = module_0.depth_first_search(node_0, list_0)
    assert var_0 is False


#@pytest.mark.xfail(strict=True)
def test_case_2():
    complex_0 = 477.927428 - 73.17813j
    list_0 = [complex_0, complex_0, complex_0, complex_0]
    none_type_0 = None
    node_0 = module_1.Node(list_0, successors=list_0, incoming_nodes=none_type_0)
    var_0 = module_0.depth_first_search(node_0, complex_0)
    assert var_0 is True
    bool_0 = True
    var_1 = module_0.depth_first_search(bool_0, bool_0)
    assert var_1 is True
#    var_1.predecessors()
