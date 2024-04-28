# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import detect_cycle as module_0
import node as module_1


def test_case_0():
    none_type_0 = None
    var_0 = module_0.detect_cycle(none_type_0)
    assert var_0 is False
    var_1 = module_0.detect_cycle(none_type_0)
    assert var_1 is False


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    var_0 = module_0.detect_cycle(none_type_0)
    assert var_0 is False
    module_0.detect_cycle(var_0)


def test_case_2():
    float_0 = -1328.238306912538
    none_type_0 = None
    node_0 = module_1.Node(predecessors=float_0)
    node_1 = module_1.Node(float_0, incoming_nodes=node_0)
    node_2 = module_1.Node(
        successor=node_1, predecessors=node_0, outgoing_nodes=none_type_0
    )
    var_0 = module_0.detect_cycle(node_2)
    assert var_0 is False
    var_1 = module_0.detect_cycle(node_1)
    assert var_1 is False


def test_case_3():
    node_0 = module_1.Node()
    node_1 = module_1.Node(successor=node_0, predecessors=node_0)
    var_0 = module_0.detect_cycle(node_1)
    assert var_0 is False