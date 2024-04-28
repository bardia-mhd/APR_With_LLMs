# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_path_length as module_0
import node as module_1


def test_case_0():
    bool_0 = True
    var_0 = module_0.shortest_path_length(bool_0, bool_0, bool_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = 'pxi"IBqCvnFU'
    float_0 = 400.155
    module_0.get(str_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    set_0 = set()
    list_0 = [set_0]
    node_0 = module_1.Node(list_0, successors=list_0)
    module_0.shortest_path_length(node_0, node_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "3h"
    module_0.insert_or_update(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    var_0 = module_0.shortest_path_length(bool_0, bool_0, bool_0)
    assert var_0 == 0
    module_0.shortest_path_length(bool_0, var_0, bool_0)


def test_case_5():
    set_0 = set()
    node_0 = module_1.Node(predecessors=set_0, outgoing_nodes=set_0)
    var_0 = module_0.shortest_path_length(node_0, node_0, set_0)
    assert var_0 == pytest.approx(1e309, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_6():
    set_0 = set()
    node_0 = module_1.Node(predecessors=set_0, outgoing_nodes=set_0)
    var_0 = module_0.shortest_path_length(node_0, node_0, set_0)
    assert var_0 == pytest.approx(1e309, abs=0.01, rel=0.01)
    list_0 = [node_0]
    list_1 = [var_0, var_0]
    list_2 = [list_1, node_0, list_1]
    module_0.get(list_2, list_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    set_0 = set()
    node_0 = module_1.Node(predecessors=set_0, outgoing_nodes=set_0)
    var_0 = module_0.shortest_path_length(node_0, node_0, set_0)
    assert var_0 == pytest.approx(1e309, abs=0.01, rel=0.01)
    str_0 = "9/"
    dict_0 = {str_0: str_0, var_0: var_0, var_0: node_0, var_0: var_0}
    list_0 = [str_0, var_0]
    var_1 = module_0.insert_or_update(list_0, str_0)
    module_0.insert_or_update(dict_0, dict_0)


def test_case_8():
    set_0 = set()
    node_0 = module_1.Node(predecessors=set_0, outgoing_nodes=set_0)
    var_0 = module_0.shortest_path_length(node_0, node_0, set_0)
    assert var_0 == pytest.approx(1e309, abs=0.01, rel=0.01)
    str_0 = "&_)S+~Oa@M&j+px"
    list_0 = [str_0, set_0]
    list_1 = [list_0, str_0, list_0]
    var_1 = module_0.get(list_1, set_0)
    assert var_1 == "&_)S+~Oa@M&j+px"


def test_case_9():
    set_0 = set()
    node_0 = module_1.Node(predecessors=set_0, outgoing_nodes=set_0)
    var_0 = module_0.shortest_path_length(node_0, node_0, set_0)
    assert var_0 == pytest.approx(1e309, abs=0.01, rel=0.01)
    str_0 = "9/"
    list_0 = [str_0, str_0, var_0, str_0, str_0]
    var_1 = module_0.insert_or_update(list_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    set_0 = set()
    node_0 = module_1.Node(predecessors=set_0, outgoing_nodes=set_0)
    var_0 = module_0.shortest_path_length(node_0, node_0, set_0)
    assert var_0 == pytest.approx(1e309, abs=0.01, rel=0.01)
    str_0 = "9/"
    module_0.insert_or_update(set_0, str_0)