# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import breadth_first_search as module_0
import node as module_1


def test_case_0():
    bool_0 = False
    var_0 = module_0.breadth_first_search(bool_0, bool_0)
    assert var_0 is True


def test_case_1():
    str_0 = "c"
    node_0 = module_1.Node(str_0, successors=str_0)
    var_0 = module_0.breadth_first_search(node_0, str_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_2():
    node_0 = module_1.Node()
    none_type_0 = None
    var_0 = module_0.breadth_first_search(node_0, none_type_0)
    assert var_0 is False
    none_type_0.successors()