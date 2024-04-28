# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_path_length as module_0
import node as module_1
import heapq as module_2


def test_case_0():
    none_type_0 = None
    var_0 = module_0.shortest_path_length(none_type_0, none_type_0, none_type_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "rx"
    module_0.get(str_0, str_0)


def test_case_2():
    set_0 = set()
    var_0 = module_0.get(set_0, set_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "rx"
    module_0.insert_or_update(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    complex_0 = 294.7733 - 339.03079139266237j
    bytes_0 = b"\xf5\xd2\x84\x1f\x81x\x7f\xbf\xca\xc0\x8f\xdc:\xdc}\x1d\xef"
    module_0.shortest_path_length(complex_0, bytes_0, complex_0)


def test_case_5():
    float_0 = -5228.37953
    node_0 = module_1.Node(float_0, float_0)
    var_0 = module_0.shortest_path_length(node_0, node_0, float_0)
    assert var_0 == pytest.approx(1e309, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_6():
    none_type_0 = None
    dict_0 = {
        none_type_0: none_type_0,
        none_type_0: none_type_0,
        none_type_0: none_type_0,
        none_type_0: none_type_0,
    }
    node_0 = module_1.Node(successor=none_type_0, successors=dict_0)
    module_0.shortest_path_length(node_0, node_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "zz0ONAr;f&T)T$]&"
    list_0 = [str_0, str_0]
    tuple_0 = (list_0,)
    var_0 = module_0.get(tuple_0, tuple_0)
    assert var_0 == 0
    complex_0 = 1059.156 + 779j
    module_0.shortest_path_length(complex_0, var_0, complex_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    var_0 = module_2.merge()
    var_1 = module_0.get(var_0, var_0)
    assert var_1 == 0
    str_0 = "zz0ONAr;f&T)T$]&"
    list_0 = [str_0, str_0]
    tuple_0 = (list_0,)
    var_2 = module_0.shortest_path_length(str_0, str_0, str_0)
    assert var_2 == 0
    var_3 = module_0.get(tuple_0, str_0)
    assert var_3 == "zz0ONAr;f&T)T$]&"
    module_0.get(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = "zz0ONAr;f&T)T$]&"
    list_0 = [str_0, str_0]
    tuple_0 = (list_0,)
    module_0.insert_or_update(tuple_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    var_0 = module_2.merge()
    var_1 = module_0.get(var_0, var_0)
    assert var_1 == 0
    list_0 = [var_1, var_1]
    var_2 = module_0.shortest_path_length(var_1, var_1, var_1)
    assert var_2 == 0
    module_0.insert_or_update(var_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_11():
    bytes_0 = b"J\xdd\x0b\x94\xe2\xdf\xfc"
    int_0 = 204
    tuple_0 = (bytes_0, int_0)
    dict_0 = {bytes_0: bytes_0, tuple_0: tuple_0}
    bool_0 = True
    tuple_1 = (dict_0, bool_0)
    module_0.insert_or_update(tuple_1, tuple_1)