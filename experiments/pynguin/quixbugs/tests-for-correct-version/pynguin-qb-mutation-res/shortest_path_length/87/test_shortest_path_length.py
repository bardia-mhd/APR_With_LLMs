# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_path_length as module_0
import heapq as module_1
import node as module_2


def test_case_0():
    none_type_0 = None
    var_0 = module_0.shortest_path_length(none_type_0, none_type_0, none_type_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    var_0 = module_1.merge()
    set_0 = {var_0, var_0, var_0}
    var_1 = module_0.get(var_0, var_0)
    assert var_1 == 0
    module_0.get(set_0, var_0)


def test_case_2():
    int_0 = -2396
    tuple_0 = (int_0, int_0)
    list_0 = [tuple_0]
    var_0 = module_0.insert_or_update(list_0, tuple_0)


def test_case_3():
    set_0 = set()
    var_0 = module_0.get(set_0, set_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_4():
    none_type_0 = None
    var_0 = module_0.shortest_path_length(none_type_0, none_type_0, none_type_0)
    assert var_0 == 0
    module_0.shortest_path_length(var_0, none_type_0, var_0)


def test_case_5():
    dict_0 = {}
    node_0 = module_2.Node(dict_0, dict_0)
    var_0 = module_0.shortest_path_length(node_0, node_0, dict_0)
    assert var_0 == pytest.approx(1e309, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_6():
    set_0 = set()
    var_0 = module_0.get(set_0, set_0)
    assert var_0 == 0
    var_1 = module_0.shortest_path_length(set_0, var_0, var_0)
    assert var_1 == 0
    bytes_0 = b""
    list_0 = [set_0, var_0]
    module_0.insert_or_update(bytes_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "J"
    none_type_0 = None
    node_0 = module_2.Node(none_type_0, str_0, str_0)
    module_0.shortest_path_length(str_0, node_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "&6"
    set_0 = {str_0, str_0, str_0, str_0}
    none_type_0 = None
    var_0 = module_0.get(set_0, none_type_0)
    assert var_0 == 0
    module_0.shortest_path_length(set_0, str_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = "S%RP0mhjdUtFj)'o"
    bool_0 = False
    tuple_0 = (bool_0, bool_0)
    dict_0 = {str_0: tuple_0, tuple_0: tuple_0}
    list_0 = [dict_0, str_0]
    var_0 = module_0.get(list_0, tuple_0)
    assert var_0 == "S%RP0mhjdUtFj)'o"
    int_0 = -683
    module_0.insert_or_update(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    bytes_0 = b"\xb0qlOF\xd0\x7f\th\xcdl\xa9PS\x80\xfc]\xe6\x8f"
    list_0 = [bytes_0, bytes_0]
    list_1 = [list_0, list_0, bytes_0, list_0]
    var_0 = module_1.merge(*list_1)
    str_0 = "- "
    module_0.insert_or_update(list_1, str_0)