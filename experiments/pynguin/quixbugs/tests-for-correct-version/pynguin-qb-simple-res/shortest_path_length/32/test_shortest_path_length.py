# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_path_length as module_0
import node as module_1
import heapq as module_2


def test_case_0():
    bool_0 = False
    var_0 = module_0.shortest_path_length(bool_0, bool_0, bool_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    tuple_0 = (none_type_0, none_type_0)
    module_0.get(tuple_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = 'n|zy9TDMkJ"$i'
    list_0 = [str_0, str_0, str_0]
    node_0 = module_1.Node(str_0, successors=list_0, incoming_nodes=str_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value == 'n|zy9TDMkJ"$i'
    assert node_0.successor is None
    assert node_0.successors == ['n|zy9TDMkJ"$i', 'n|zy9TDMkJ"$i', 'n|zy9TDMkJ"$i']
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == 'n|zy9TDMkJ"$i'
    assert node_0.outgoing_nodes == []
    module_0.shortest_path_length(list_0, node_0, list_0)


def test_case_3():
    node_0 = module_1.Node()
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    bool_0 = False
    var_0 = module_0.shortest_path_length(bool_0, node_0, bool_0)
    assert var_0 == pytest.approx(1e309, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = 'Fn|fzy9TDMkJ"$i'
    list_0 = [str_0, str_0]
    int_0 = 1737
    bytes_0 = b"\xa0\xc6B\xd6\x0c\xc3v\xaa"
    tuple_0 = (list_0, int_0, bytes_0, str_0)
    module_0.get(tuple_0, tuple_0)


def test_case_5():
    str_0 = 'Fn|fzy9TDMkJ"$i'
    list_0 = [str_0, str_0]
    int_0 = 1737
    list_1 = [list_0, int_0]
    var_0 = module_0.insert_or_update(list_1, list_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = 'Fn|fzy9TDMkJ"$i'
    list_0 = [str_0, str_0]
    int_0 = 1737
    list_1 = [list_0, int_0]
    none_type_0 = None
    var_0 = module_0.shortest_path_length(str_0, none_type_0, none_type_0)
    assert var_0 == 0
    var_1 = module_0.insert_or_update(list_1, list_0)
    module_0.insert_or_update(list_1, list_1)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "\\u>!*3 v0\x0bU+7K"
    list_0 = [str_0, str_0]
    list_1 = [list_0, list_0, list_0, str_0]
    var_0 = module_0.get(list_1, str_0)
    assert var_0 == "\\u>!*3 v0\x0bU+7K"
    node_0 = module_1.Node(str_0, successors=list_0, incoming_nodes=var_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value == "\\u>!*3 v0\x0bU+7K"
    assert node_0.successor is None
    assert node_0.successors == ["\\u>!*3 v0\x0bU+7K", "\\u>!*3 v0\x0bU+7K"]
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == "\\u>!*3 v0\x0bU+7K"
    assert node_0.outgoing_nodes == []
    module_0.shortest_path_length(list_1, node_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = 'Fn|fzy9TDMkJ"$i'
    list_0 = [str_0, str_0]
    list_1 = [list_0, list_0, list_0, str_0]
    var_0 = module_0.get(list_1, str_0)
    assert var_0 == 'Fn|fzy9TDMkJ"$i'
    var_1 = module_0.shortest_path_length(list_0, list_0, list_0)
    assert var_1 == 0
    list_2 = module_2.merge()
    none_type_0 = None
    var_2 = module_0.shortest_path_length(str_0, none_type_0, none_type_0)
    assert var_2 == 0
    module_0.insert_or_update(list_2, list_0)