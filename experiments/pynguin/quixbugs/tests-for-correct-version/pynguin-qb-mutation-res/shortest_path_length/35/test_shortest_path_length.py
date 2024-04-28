# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_path_length as module_0
import node as module_1


def test_case_0():
    list_0 = []
    var_0 = module_0.shortest_path_length(list_0, list_0, list_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 1263
    tuple_0 = (int_0, int_0)
    list_0 = [tuple_0, int_0, int_0, int_0]
    none_type_0 = None
    module_0.get(list_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"U\xe7\xe0\xfdZ!~"
    node_0 = module_1.Node(
        successors=bytes_0, predecessors=bytes_0, outgoing_nodes=bytes_0
    )
    module_0.shortest_path_length(bytes_0, node_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 1263
    tuple_0 = (int_0, int_0)
    module_0.insert_or_update(tuple_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xecNl\xe3.\xc8\xd2R\xbf\x89"
    module_0.insert_or_update(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = True
    none_type_0 = None
    module_0.shortest_path_length(bool_0, none_type_0, bool_0)


def test_case_6():
    node_0 = module_1.Node()
    var_0 = module_0.shortest_path_length(node_0, node_0, node_0)
    assert var_0 == 0
    list_0 = []
    set_0 = {var_0, node_0, var_0}
    var_1 = module_0.insert_or_update(list_0, set_0)
    var_2 = module_0.insert_or_update(list_0, set_0)


def test_case_7():
    tuple_0 = ()
    node_0 = module_1.Node()
    var_0 = module_0.shortest_path_length(node_0, node_0, tuple_0)
    assert var_0 == pytest.approx(1e309, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_8():
    int_0 = 1263
    tuple_0 = (int_0, int_0)
    list_0 = [tuple_0, int_0, int_0, int_0]
    var_0 = module_0.get(list_0, int_0)
    assert var_0 == 1263
    none_type_0 = None
    module_0.get(list_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    tuple_0 = ()
    node_0 = module_1.Node()
    var_0 = module_0.shortest_path_length(tuple_0, node_0, tuple_0)
    assert var_0 == pytest.approx(1e309, abs=0.01, rel=0.01)
    dict_0 = {node_0: node_0, tuple_0: node_0}
    list_0 = [dict_0]
    set_0 = {var_0, node_0, var_0}
    module_0.insert_or_update(list_0, set_0)