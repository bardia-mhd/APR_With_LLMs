# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_path_length as module_0
import node as module_1


def test_case_0():
    int_0 = 608
    var_0 = module_0.shortest_path_length(int_0, int_0, int_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "<_ZpT}& v'"
    node_0 = module_1.Node(str_0, str_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value == "<_ZpT}& v'"
    assert node_0.successor == "<_ZpT}& v'"
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    module_0.get(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = '*]_z` Qf"*RLl:<'
    none_type_0 = None
    node_0 = module_1.Node(none_type_0, str_0, str_0, outgoing_nodes=str_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor == '*]_z` Qf"*RLl:<'
    assert node_0.successors == '*]_z` Qf"*RLl:<'
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == '*]_z` Qf"*RLl:<'
    module_0.shortest_path_length(node_0, node_0, str_0)


def test_case_3():
    str_0 = '*]_z` Qf"*RLl:<'
    node_0 = module_1.Node(str_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value == '*]_z` Qf"*RLl:<'
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    var_0 = module_0.shortest_path_length(node_0, node_0, str_0)
    assert var_0 == pytest.approx(1e309, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_4():
    set_0 = set()
    bool_0 = False
    tuple_0 = (bool_0,)
    bytes_0 = b""
    tuple_1 = (tuple_0, bytes_0)
    module_0.insert_or_update(set_0, tuple_1)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = False
    float_0 = 102.0924
    set_0 = {bool_0, bool_0, bool_0, float_0}
    module_0.insert_or_update(set_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    bool_0 = True
    none_type_0 = None
    dict_0 = {
        none_type_0: none_type_0,
        none_type_0: bool_0,
        bool_0: none_type_0,
        none_type_0: none_type_0,
    }
    bytes_0 = b"r:"
    tuple_0 = (dict_0, bytes_0)
    var_0 = module_0.get(tuple_0, bool_0)
    module_0.get(bool_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    dict_0 = {}
    var_0 = module_0.get(dict_0, dict_0)
    assert var_0 == 0
    var_1 = module_0.get(dict_0, dict_0)
    assert var_1 == 0
    dict_1 = {var_1: var_1}
    bool_0 = False
    list_0 = [var_1, dict_1]
    list_1 = []
    var_2 = module_0.get(dict_0, var_1)
    assert var_2 == 0
    var_3 = module_0.shortest_path_length(list_0, list_1, list_1)
    assert var_3 == 0
    node_0 = module_1.Node(var_3, incoming_nodes=var_3)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value == 0
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == 0
    assert node_0.outgoing_nodes == []
    var_4 = module_0.shortest_path_length(bool_0, node_0, dict_0)
    assert var_4 == pytest.approx(1e309, abs=0.01, rel=0.01)
    var_5 = module_0.insert_or_update(list_1, list_0)
    var_6 = module_0.get(list_1, dict_0)
    assert var_6 == 0
    module_0.shortest_path_length(var_6, list_1, var_3)


@pytest.mark.xfail(strict=True)
def test_case_8():
    dict_0 = {}
    var_0 = module_0.get(dict_0, dict_0)
    assert var_0 == 0
    list_0 = [var_0, dict_0]
    list_1 = [list_0, var_0]
    var_1 = module_0.shortest_path_length(list_0, list_1, list_1)
    assert var_1 == 0
    node_0 = module_1.Node(var_1, incoming_nodes=var_1)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value == 0
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == 0
    assert node_0.outgoing_nodes == []
    var_2 = module_0.shortest_path_length(var_1, node_0, dict_0)
    assert var_2 == pytest.approx(1e309, abs=0.01, rel=0.01)
    var_3 = module_0.insert_or_update(list_1, list_0)
    module_0.shortest_path_length(var_0, var_1, var_3)


@pytest.mark.xfail(strict=True)
def test_case_9():
    dict_0 = {}
    var_0 = module_0.get(dict_0, dict_0)
    assert var_0 == 0
    list_0 = [var_0, dict_0]
    list_1 = [list_0, var_0]
    var_1 = module_0.shortest_path_length(list_0, list_1, list_1)
    assert var_1 == 0
    module_0.insert_or_update(list_1, list_1)