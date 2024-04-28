# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_path_length as module_0
import node as module_1


def test_case_0():
    str_0 = "T"
    var_0 = module_0.shortest_path_length(str_0, str_0, str_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "T"
    var_0 = module_0.shortest_path_length(str_0, str_0, str_0)
    assert var_0 == 0
    module_0.get(str_0, str_0)


def test_case_2():
    set_0 = set()
    var_0 = module_0.get(set_0, set_0)
    assert var_0 == 0
    node_0 = module_1.Node(set_0, predecessors=set_0)
    var_1 = module_0.shortest_path_length(set_0, node_0, set_0)
    assert var_1 == pytest.approx(1e309, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "$T"
    module_0.insert_or_update(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    none_type_0 = None
    module_0.insert_or_update(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 193
    none_type_0 = None
    module_0.shortest_path_length(int_0, int_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "TS"
    var_0 = module_0.shortest_path_length(str_0, str_0, str_0)
    assert var_0 == 0
    tuple_0 = (str_0, var_0)
    list_0 = [tuple_0, str_0]
    var_1 = module_0.get(list_0, var_0)
    assert var_1 == "TS"
    var_2 = module_0.insert_or_update(list_0, str_0)
    node_0 = module_1.Node(successor=list_0, successors=tuple_0)
    assert node_0.successor == [("TS", 0), "TS"]
    assert node_0.successors == ("TS", 0)
    float_0 = 3024.06397
    module_0.shortest_path_length(node_0, node_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "TS"
    float_0 = 2946.712695
    tuple_0 = (str_0, float_0)
    list_0 = [tuple_0, tuple_0, str_0]
    var_0 = module_0.insert_or_update(list_0, str_0)
    str_1 = "T"
    var_1 = module_0.shortest_path_length(str_1, str_1, str_1)
    assert var_1 == 0
    var_1.predecessors()


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "TS"
    float_0 = 2946.712695
    tuple_0 = (str_0, float_0)
    module_0.get(tuple_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = ""
    float_0 = 270.172
    tuple_0 = (str_0, float_0)
    module_0.insert_or_update(str_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    float_0 = 2946.712695
    tuple_0 = (float_0, float_0)
    node_0 = module_1.Node(successor=float_0, successors=tuple_0)
    module_0.shortest_path_length(node_0, node_0, float_0)


def test_case_11():
    set_0 = set()
    node_0 = module_1.Node(set_0, predecessors=set_0)
    var_0 = module_0.shortest_path_length(set_0, node_0, set_0)
    assert var_0 == pytest.approx(1e309, abs=0.01, rel=0.01)