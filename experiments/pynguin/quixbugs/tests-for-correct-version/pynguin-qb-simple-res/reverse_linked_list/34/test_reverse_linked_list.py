# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import reverse_linked_list as module_0
import node as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    module_0.reverse_linked_list(bool_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.reverse_linked_list(none_type_0)


def test_case_2():
    bytes_0 = b"[&\x137\xa6D\xaf\xb6\xf6\x05\x06\xe7\xf9R"
    dict_0 = {bytes_0: bytes_0}
    set_0 = {bytes_0}
    str_0 = " @T7y)vCLhn3\r^<2rQ~i"
    int_0 = -853
    tuple_0 = (dict_0, set_0, str_0, int_0)
    tuple_1 = (tuple_0,)
    list_0 = [tuple_1, set_0, str_0]
    node_0 = module_1.Node(list_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value == [
        (
            (
                {
                    b"[&\x137\xa6D\xaf\xb6\xf6\x05\x06\xe7\xf9R": b"[&\x137\xa6D\xaf\xb6\xf6\x05\x06\xe7\xf9R"
                },
                {b"[&\x137\xa6D\xaf\xb6\xf6\x05\x06\xe7\xf9R"},
                " @T7y)vCLhn3\r^<2rQ~i",
                -853,
            ),
        ),
        {b"[&\x137\xa6D\xaf\xb6\xf6\x05\x06\xe7\xf9R"},
        " @T7y)vCLhn3\r^<2rQ~i",
    ]
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    var_0 = module_0.reverse_linked_list(node_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value == [
        (
            (
                {
                    b"[&\x137\xa6D\xaf\xb6\xf6\x05\x06\xe7\xf9R": b"[&\x137\xa6D\xaf\xb6\xf6\x05\x06\xe7\xf9R"
                },
                {b"[&\x137\xa6D\xaf\xb6\xf6\x05\x06\xe7\xf9R"},
                " @T7y)vCLhn3\r^<2rQ~i",
                -853,
            ),
        ),
        {b"[&\x137\xa6D\xaf\xb6\xf6\x05\x06\xe7\xf9R"},
        " @T7y)vCLhn3\r^<2rQ~i",
    ]
    assert var_0.successor is None
    assert var_0.successors == []
    assert var_0.predecessors == []
    assert var_0.incoming_nodes == []
    assert var_0.outgoing_nodes == []


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -591
    none_type_0 = None
    var_0 = module_1.Node(
        successor=int_0, successors=none_type_0, predecessors=none_type_0
    )
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value is None
    assert var_0.successor == -591
    assert var_0.successors is None
    assert var_0.predecessors is None
    assert var_0.incoming_nodes == []
    assert var_0.outgoing_nodes == []
    module_0.reverse_linked_list(var_0)