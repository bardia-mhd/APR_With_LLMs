# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_paths as module_0
import node as module_1


def test_case_0():
    tuple_0 = ()
    var_0 = module_0.shortest_paths(tuple_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    node_0 = module_1.Node(dict_0, successors=bool_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value == {True: True}
    assert node_0.successor is None
    assert node_0.successors is True
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    module_0.shortest_paths(node_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -691
    module_0.shortest_paths(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "/q\\yj"
    tuple_0 = (str_0, str_0)
    tuple_1 = (tuple_0, tuple_0)
    var_0 = module_0.shortest_paths(str_0, tuple_1)
    bool_0 = True
    set_0 = set()
    var_1 = module_0.shortest_paths(bool_0, set_0)
    module_0.shortest_paths(tuple_0, tuple_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "/q9kL\\Lj"
    tuple_0 = (str_0, str_0)
    dict_0 = {tuple_0: str_0}
    module_0.shortest_paths(tuple_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = ""
    tuple_0 = (str_0, str_0)
    dict_0 = module_0.shortest_paths(tuple_0, str_0)
    var_0 = module_0.shortest_paths(tuple_0, dict_0)
    tuple_1 = (tuple_0, tuple_0)
    var_1 = module_0.shortest_paths(str_0, tuple_1)
    module_0.shortest_paths(tuple_1, tuple_1)