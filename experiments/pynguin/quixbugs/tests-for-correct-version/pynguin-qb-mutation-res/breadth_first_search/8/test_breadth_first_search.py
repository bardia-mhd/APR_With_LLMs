# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import breadth_first_search as module_0
import node as module_1


def test_case_0():
    int_0 = -800
    var_0 = module_0.breadth_first_search(int_0, int_0)
    assert var_0 is True


def test_case_1():
    str_0 = "\x0bG[2*"
    node_0 = module_1.Node(outgoing_nodes=str_0)
    var_0 = module_0.breadth_first_search(node_0, str_0)
    assert var_0 is False


def test_case_2():
    str_0 = "F"
    node_0 = module_1.Node(str_0, str_0, str_0)
    var_0 = module_0.breadth_first_search(node_0, str_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "b"
    node_0 = module_1.Node(successors=str_0)
    list_0 = [node_0, node_0]
    none_type_0 = None
    node_1 = module_1.Node(
        successor=list_0, successors=list_0, outgoing_nodes=none_type_0
    )
    module_0.breadth_first_search(node_1, none_type_0)