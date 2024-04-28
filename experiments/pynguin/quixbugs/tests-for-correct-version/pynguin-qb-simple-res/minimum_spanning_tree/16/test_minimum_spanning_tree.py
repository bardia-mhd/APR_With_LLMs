# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import minimum_spanning_tree as module_0
import node as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    tuple_0 = ()
    dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0}
    var_0 = module_0.minimum_spanning_tree(tuple_0)
    module_0.minimum_spanning_tree(dict_0)


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.minimum_spanning_tree(tuple_0)
    var_1 = module_1.Node(incoming_nodes=var_0)
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "node.Node"
    assert var_1.value is None
    assert var_1.successor is None
    assert var_1.successors == []
    assert var_1.predecessors == []
    assert var_1.incoming_nodes == {*()}
    assert var_1.outgoing_nodes == []


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -1805.5
    module_0.minimum_spanning_tree(float_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    bytes_0 = b"R\x15\x8a\xc2U&\xbb\xc9\xcf\xad\x91\xa5\xde\xee\xd1X}\xde\xf3E"
    tuple_0 = (bool_0, bytes_0)
    dict_0 = {tuple_0: bool_0}
    var_0 = module_0.minimum_spanning_tree(dict_0)
    tuple_1 = ()
    var_1 = module_0.minimum_spanning_tree(tuple_1)
    module_0.minimum_spanning_tree(var_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    tuple_0 = (bool_0, bool_0)
    dict_0 = {tuple_0: bool_0}
    var_0 = module_0.minimum_spanning_tree(dict_0)
    var_0.predecessors()