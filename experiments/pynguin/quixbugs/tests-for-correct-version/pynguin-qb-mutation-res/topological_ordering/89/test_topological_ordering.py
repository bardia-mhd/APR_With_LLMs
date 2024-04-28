# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import topological_ordering as module_0
import node as module_1


def test_case_0():
    dict_0 = {}
    var_0 = module_0.topological_ordering(dict_0)
    var_1 = module_0.topological_ordering(var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 3076
    set_0 = {int_0, int_0, int_0, int_0}
    module_0.topological_ordering(set_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.topological_ordering(none_type_0)


def test_case_3():
    dict_0 = {}
    node_0 = module_1.Node(outgoing_nodes=dict_0)
    dict_1 = {node_0: node_0, node_0: dict_0}
    var_0 = module_0.topological_ordering(dict_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = -186.444351
    node_0 = module_1.Node(incoming_nodes=float_0)
    float_1 = -943.445265
    tuple_0 = (node_0, float_1, node_0)
    module_0.topological_ordering(tuple_0)


def test_case_5():
    bool_0 = False
    node_0 = module_1.Node(successors=bool_0)
    tuple_0 = (node_0, node_0, node_0)
    node_1 = module_1.Node(
        bool_0,
        tuple_0,
        predecessors=node_0,
        incoming_nodes=bool_0,
        outgoing_nodes=tuple_0,
    )
    tuple_1 = (node_1, node_1)
    var_0 = module_0.topological_ordering(tuple_1)