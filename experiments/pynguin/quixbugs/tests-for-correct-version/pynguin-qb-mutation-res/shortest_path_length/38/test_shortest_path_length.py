# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_path_length as module_0
import node as module_1


def test_case_0():
    none_type_0 = None
    var_0 = module_0.shortest_path_length(none_type_0, none_type_0, none_type_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x896\x94zy\x97\xb2\x8ey]\xa1\x0cC\xfb8\xf2\xeb\xa3\x91"
    set_0 = {bytes_0, bytes_0}
    module_0.get(set_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = '1"'
    module_0.insert_or_update(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    module_0.insert_or_update(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    none_type_0 = None
    module_0.shortest_path_length(bool_0, bool_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "fXmLh9h"
    node_0 = module_1.Node(successors=str_0, outgoing_nodes=str_0)
    module_0.shortest_path_length(node_0, node_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = ">0\x0cCSU5-E"
    none_type_0 = None
    dict_0 = {none_type_0: none_type_0, str_0: str_0}
    list_0 = [dict_0, dict_0, str_0, dict_0]
    module_0.get(list_0, none_type_0)


def test_case_7():
    str_0 = ">0CSU5-E"
    var_0 = module_0.shortest_path_length(str_0, str_0, str_0)
    assert var_0 == 0
    none_type_0 = None
    dict_0 = {none_type_0: none_type_0, str_0: str_0}
    list_0 = [dict_0, var_0, str_0, dict_0]
    var_1 = module_0.get(list_0, str_0)


def test_case_8():
    str_0 = ""
    node_0 = module_1.Node(successors=str_0, outgoing_nodes=str_0)
    var_0 = module_0.shortest_path_length(node_0, node_0, str_0)
    assert var_0 == pytest.approx(1e309, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = ""
    none_type_0 = None
    set_0 = {str_0, str_0, str_0, none_type_0}
    module_0.insert_or_update(str_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    float_0 = 458.36
    set_0 = {float_0}
    list_0 = [set_0, float_0]
    dict_0 = {}
    tuple_0 = (list_0, dict_0)
    module_0.insert_or_update(tuple_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_11():
    float_0 = 458.36
    set_0 = {float_0}
    list_0 = [set_0, float_0]
    dict_0 = {}
    tuple_0 = (list_0, dict_0)
    module_0.insert_or_update(tuple_0, list_0)