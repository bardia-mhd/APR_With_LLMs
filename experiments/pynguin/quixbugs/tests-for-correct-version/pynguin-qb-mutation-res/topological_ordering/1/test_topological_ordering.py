# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import topological_ordering as module_0
import node as module_1


def test_case_0():
    dict_0 = {}
    var_0 = module_0.topological_ordering(dict_0)


def test_case_1():
    node_0 = module_1.Node()
    dict_0 = {node_0: node_0}
    var_0 = module_0.topological_ordering(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.topological_ordering(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    bytes_0 = b"\x16\xf2\xfcK\x9c2\xc5@"
    node_0 = module_1.Node(
        successors=none_type_0, predecessors=none_type_0, outgoing_nodes=bytes_0
    )
    dict_0 = {node_0: node_0}
    module_0.topological_ordering(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x1f\xed\xde\xe5\x0bm;\xbd\xf7*\xf4"
    dict_0 = {bytes_0: bytes_0}
    node_0 = module_1.Node(predecessors=dict_0, incoming_nodes=dict_0)
    str_0 = ""
    bool_0 = True
    tuple_0 = (node_0, str_0, bool_0)
    module_0.topological_ordering(tuple_0)