# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_path_length as module_0
import node as module_1
import heapq as module_2


def test_case_0():
    float_0 = -3247.3
    var_0 = module_0.shortest_path_length(float_0, float_0, float_0)
    assert var_0 == 0


def test_case_1():
    str_0 = "b,"
    set_0 = {str_0, str_0, str_0}
    var_0 = module_0.get(set_0, set_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    dict_0 = {}
    var_0 = module_0.get(dict_0, dict_0)
    assert var_0 == 0
    module_0.get(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = -3247.3
    var_0 = module_0.shortest_path_length(float_0, float_0, float_0)
    assert var_0 == 0
    module_0.shortest_path_length(float_0, var_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "b,"
    set_0 = {str_0, str_0, str_0}
    module_0.insert_or_update(set_0, str_0)


def test_case_5():
    str_0 = "pN 3\nBYV"
    node_0 = module_1.Node(str_0, incoming_nodes=str_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value == "pN 3\nBYV"
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == "pN 3\nBYV"
    assert node_0.outgoing_nodes == []
    var_0 = module_0.shortest_path_length(node_0, node_0, str_0)
    assert var_0 == pytest.approx(1e309, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_6():
    bytes_0 = b"\xaf\x13"
    set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
    var_0 = module_0.shortest_path_length(bytes_0, bytes_0, bytes_0)
    assert var_0 == 0
    var_1 = module_0.shortest_path_length(var_0, var_0, var_0)
    assert var_1 == 0
    var_2 = module_0.get(set_0, var_0)
    assert var_2 == 0
    var_3 = module_2.merge()
    module_0.insert_or_update(var_3, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    bytes_0 = b"_\x14"
    set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
    var_0 = module_0.get(set_0, set_0)
    assert var_0 == 0
    var_1 = module_0.get(set_0, var_0)
    assert var_1 == 0
    tuple_0 = (bytes_0, var_1)
    module_0.insert_or_update(set_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "pN 3BYV"
    node_0 = module_1.Node(str_0, successors=str_0, incoming_nodes=str_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value == "pN 3BYV"
    assert node_0.successor is None
    assert node_0.successors == "pN 3BYV"
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == "pN 3BYV"
    assert node_0.outgoing_nodes == []
    module_0.shortest_path_length(node_0, node_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    bytes_0 = b"\xed\x00"
    set_0 = {bytes_0, bytes_0, bytes_0, bytes_0, bytes_0}
    bool_0 = False
    var_0 = module_0.get(set_0, bool_0)
    assert var_0 == 237
    module_0.insert_or_update(set_0, var_0)