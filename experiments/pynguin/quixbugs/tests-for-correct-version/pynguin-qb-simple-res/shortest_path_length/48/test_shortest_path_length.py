# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_path_length as module_0
import heapq as module_1
import node as module_2


def test_case_0():
    bool_0 = True
    var_0 = module_0.shortest_path_length(bool_0, bool_0, bool_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    var_0 = module_1.merge()
    list_0 = [var_0, var_0, var_0, var_0]
    module_0.get(list_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    set_0 = set()
    var_0 = module_0.get(set_0, set_0)
    assert var_0 == 0
    tuple_0 = (set_0, set_0)
    module_0.get(tuple_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 2308
    module_0.get(int_0, int_0)


def test_case_4():
    int_0 = 3640
    node_0 = module_2.Node(incoming_nodes=int_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == 3640
    assert node_0.outgoing_nodes == []
    var_0 = module_0.shortest_path_length(node_0, node_0, int_0)
    assert var_0 == pytest.approx(1e309, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"x\xb1"
    module_0.insert_or_update(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    int_0 = 1746
    list_0 = [int_0, int_0]
    str_0 = "=VBF1qvrWW}R"
    bool_0 = False
    tuple_0 = (list_0, str_0, bool_0, int_0)
    var_0 = module_1.merge(*list_0)
    module_0.get(tuple_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    set_0 = set()
    none_type_0 = None
    node_0 = module_2.Node(outgoing_nodes=none_type_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes is None
    var_0 = module_0.get(set_0, set_0)
    assert var_0 == 0
    var_1 = module_0.shortest_path_length(set_0, node_0, var_0)
    assert var_1 == pytest.approx(1e309, abs=0.01, rel=0.01)
    var_2 = module_0.shortest_path_length(node_0, node_0, var_0)
    assert var_2 == pytest.approx(1e309, abs=0.01, rel=0.01)
    tuple_0 = (var_2, var_2)
    set_1 = {var_2, tuple_0}
    module_0.insert_or_update(set_1, set_1)


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "-/ \t|G"
    set_0 = set()
    node_0 = module_2.Node(outgoing_nodes=str_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == "-/ \t|G"
    var_0 = module_0.get(set_0, set_0)
    assert var_0 == 0
    var_1 = module_0.shortest_path_length(set_0, node_0, var_0)
    assert var_1 == pytest.approx(1e309, abs=0.01, rel=0.01)
    var_2 = module_0.shortest_path_length(node_0, node_0, var_0)
    assert var_2 == pytest.approx(1e309, abs=0.01, rel=0.01)
    tuple_0 = (var_2, var_0)
    set_1 = {var_2, tuple_0}
    module_0.insert_or_update(set_1, set_1)


@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = "P\t\x0b;\\\"P3uw'"
    none_type_0 = None
    node_0 = module_2.Node(
        successor=none_type_0, successors=str_0, outgoing_nodes=none_type_0
    )
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == "P\t\x0b;\\\"P3uw'"
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes is None
    module_0.shortest_path_length(str_0, node_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    str_0 = "-/ \t|G"
    var_0 = module_0.shortest_path_length(str_0, str_0, str_0)
    assert var_0 == 0
    set_0 = set()
    node_0 = module_2.Node(outgoing_nodes=var_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == 0
    var_1 = module_0.get(set_0, set_0)
    assert var_1 == 0
    var_2 = module_0.shortest_path_length(set_0, node_0, var_1)
    assert var_2 == pytest.approx(1e309, abs=0.01, rel=0.01)
    var_3 = module_0.shortest_path_length(node_0, node_0, var_1)
    assert var_3 == pytest.approx(1e309, abs=0.01, rel=0.01)
    tuple_0 = (var_3, var_3)
    set_1 = {var_3, tuple_0}
    var_4 = module_0.get(set_1, var_2)
    assert var_4 == pytest.approx(1e309, abs=0.01, rel=0.01)
    var_0.predecessors()


@pytest.mark.xfail(strict=True)
def test_case_11():
    set_0 = set()
    tuple_0 = (set_0, set_0)
    module_0.insert_or_update(set_0, tuple_0)