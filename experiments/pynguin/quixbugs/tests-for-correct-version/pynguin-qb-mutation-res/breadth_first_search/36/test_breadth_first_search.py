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
    bytes_0 = b"\x95p\x8b\xab"
    node_0 = module_1.Node(
        successor=bytes_0,
        successors=bytes_0,
        predecessors=bytes_0,
        incoming_nodes=bytes_0,
    )
    module_0.breadth_first_search(node_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x9bDE\t\xf0 \xe4h-\xb9\xb8\xfe\xbd"
    node_0 = module_1.Node(bytes_0, bytes_0, outgoing_nodes=bytes_0)
    var_0 = module_0.breadth_first_search(node_0, bytes_0)
    assert var_0 is False
    var_0.predecessors()