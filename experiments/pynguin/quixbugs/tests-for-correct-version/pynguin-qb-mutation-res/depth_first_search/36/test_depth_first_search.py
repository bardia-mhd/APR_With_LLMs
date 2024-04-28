# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import depth_first_search as module_0
import node as module_1


def test_case_0():
    bytes_0 = b"\x1d\x93A\xc5"
    var_0 = module_0.depth_first_search(bytes_0, bytes_0)
    assert var_0 is True


def test_case_1():
    bytes_0 = b"\xe8DY\x8a<\x84\xb7\x17"
    node_0 = module_1.Node(
        successor=bytes_0, predecessors=bytes_0, incoming_nodes=bytes_0
    )
    var_0 = module_0.depth_first_search(node_0, bytes_0)
    assert var_0 is False
    tuple_0 = ()
    var_1 = module_0.depth_first_search(tuple_0, tuple_0)
    assert var_1 is True


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 229
    none_type_0 = None
    module_0.depth_first_search(int_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "z"
    var_0 = module_0.depth_first_search(str_0, str_0)
    assert var_0 is True
    str_1 = "e]w9HBq.% @xoya]>(?Z"
    var_1 = module_1.Node(str_0, str_1, str_0)
    var_2 = module_0.depth_first_search(var_1, str_0)
    assert var_2 is True
    node_0 = module_1.Node(successors=str_0, predecessors=var_0)
    assert node_0.predecessors is True
    var_3 = module_0.depth_first_search(var_2, var_2)
    assert var_3 is True
    bool_0 = True
    var_4 = module_0.depth_first_search(var_2, bool_0)
    assert var_4 is True
    module_0.depth_first_search(node_0, var_2)