# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import breadth_first_search as module_0
import node as module_1


def test_case_0():
    none_type_0 = None
    var_0 = module_0.breadth_first_search(none_type_0, none_type_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x02\xc8{\xf2\x0e%f\x8dN\xda\x0c.\x1e\xfeicC\xc4"
    node_0 = module_1.Node(successors=bytes_0, incoming_nodes=bytes_0)
    module_0.breadth_first_search(node_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    none_type_0 = None
    module_0.breadth_first_search(bool_0, none_type_0)


def test_case_3():
    bool_0 = True
    tuple_0 = (bool_0, bool_0, bool_0)
    node_0 = module_1.Node(predecessors=tuple_0, incoming_nodes=bool_0)
    var_0 = module_0.breadth_first_search(node_0, tuple_0)
    assert var_0 is False