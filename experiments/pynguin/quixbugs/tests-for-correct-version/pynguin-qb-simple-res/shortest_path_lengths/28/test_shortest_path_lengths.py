# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_path_lengths as module_0
import collections as module_1
import node as module_2


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 666
    module_0.shortest_path_lengths(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.shortest_path_lengths(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    dict_1 = module_0.shortest_path_lengths(bool_0, dict_0)
    assert (
        f"{type(dict_1).__module__}.{type(dict_1).__qualname__}"
        == "collections.defaultdict"
    )
    assert len(dict_1) == 2
    assert (
        f"{type(module_1.defaultdict.default_factory).__module__}.{type(module_1.defaultdict.default_factory).__qualname__}"
        == "builtins.member_descriptor"
    )
    node_0 = module_2.Node(successor=dict_1, outgoing_nodes=dict_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert (
        f"{type(node_0.successor).__module__}.{type(node_0.successor).__qualname__}"
        == "collections.defaultdict"
    )
    assert len(node_0.successor) == 2
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == {True: True}
    node_0.predecessors()