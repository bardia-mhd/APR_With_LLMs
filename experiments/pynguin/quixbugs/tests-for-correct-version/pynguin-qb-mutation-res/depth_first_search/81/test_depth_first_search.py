# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import depth_first_search as module_0
import node as module_1


def test_case_0():
    none_type_0 = None
    var_0 = module_0.depth_first_search(none_type_0, none_type_0)
    assert var_0 is True


def test_case_1():
    str_0 = "#d2@B)z/.Z^5A\\"
    node_0 = module_1.Node(str_0)
    var_0 = module_0.depth_first_search(node_0, str_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    bytes_0 = b"\xf0\xa4\t\xb6\xd32\xb2OR\x8b\xef"
    node_0 = module_1.Node(none_type_0, successors=bytes_0, predecessors=bytes_0)
    module_0.depth_first_search(node_0, none_type_0)