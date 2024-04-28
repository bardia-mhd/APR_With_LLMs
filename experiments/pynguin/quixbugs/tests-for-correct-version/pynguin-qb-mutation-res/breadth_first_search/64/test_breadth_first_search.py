# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import breadth_first_search as module_0
import node as module_1


def test_case_0():
    float_0 = -396.458
    var_0 = module_0.breadth_first_search(float_0, float_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "y&"
    node_0 = module_1.Node(successors=str_0, predecessors=str_0)
    module_0.breadth_first_search(node_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 582
    none_type_0 = None
    module_0.breadth_first_search(int_0, none_type_0)


def test_case_3():
    bytes_0 = b"\xe0d\xe1\xf0\x07~2\xd6\x83\xa7\xba\xdfh\x86[0\x0e"
    node_0 = module_1.Node(incoming_nodes=bytes_0, outgoing_nodes=bytes_0)
    list_0 = []
    list_1 = [node_0, bytes_0, list_0, node_0]
    var_0 = module_0.breadth_first_search(node_0, list_1)
    assert var_0 is False


def test_case_4():
    str_0 = "C"
    node_0 = module_1.Node(successor=str_0, successors=str_0)
    var_0 = module_0.breadth_first_search(node_0, str_0)
    assert var_0 is True
    list_0 = [node_0, str_0]
    node_1 = module_1.Node(successors=list_0)
    var_1 = module_0.breadth_first_search(node_1, str_0)
    assert var_1 is True