# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import detect_cycle as module_0
import node as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    var_0 = module_0.detect_cycle(none_type_0)
    assert var_0 is False
    bool_0 = True
    module_0.detect_cycle(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    module_0.detect_cycle(tuple_0)


def test_case_2():
    bool_0 = True
    node_0 = module_1.Node(bool_0, predecessors=bool_0, incoming_nodes=bool_0)
    node_1 = module_1.Node(successor=node_0, successors=node_0)
    var_0 = module_0.detect_cycle(node_1)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    node_0 = module_1.Node(bool_0, predecessors=bool_0, incoming_nodes=bool_0)
    node_1 = module_1.Node(successor=node_0, successors=node_0)
    var_0 = module_0.detect_cycle(node_1)
    assert var_0 is False
    var_1 = module_0.detect_cycle(node_0)
    assert var_1 is False
    var_1.predecessors()