# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import depth_first_search as module_0
import node as module_1


def test_case_0():
    none_type_0 = None
    var_0 = module_0.depth_first_search(none_type_0, none_type_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    node_0 = module_1.Node(predecessors=none_type_0, incoming_nodes=none_type_0)
    var_0 = module_0.depth_first_search(node_0, none_type_0)
    assert var_0 is False
    var_0.successor()


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    set_0 = {none_type_0, none_type_0, none_type_0, none_type_0}
    module_0.depth_first_search(none_type_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    set_0 = {bool_0, bool_0}
    var_0 = module_1.Node(successors=bool_0)
    node_0 = module_1.Node(set_0, var_0, set_0, incoming_nodes=set_0)
    module_0.depth_first_search(node_0, var_0)