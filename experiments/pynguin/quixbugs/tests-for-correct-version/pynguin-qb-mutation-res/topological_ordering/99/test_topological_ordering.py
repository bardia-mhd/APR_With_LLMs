# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import topological_ordering as module_0
import node as module_1
import builtins as module_2


def test_case_0():
    str_0 = ""
    var_0 = module_0.topological_ordering(str_0)
    var_1 = module_0.topological_ordering(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    complex_0 = -1955.9528 - 3404j
    list_0 = [complex_0, complex_0, complex_0]
    module_0.topological_ordering(list_0)


def test_case_2():
    node_0 = module_1.Node()
    dict_0 = {node_0: node_0, node_0: node_0, node_0: node_0}
    var_0 = module_0.topological_ordering(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "fm\\R@<wR\te8$"
    none_type_0 = None
    node_0 = module_1.Node(none_type_0, incoming_nodes=str_0)
    dict_0 = {node_0: str_0, node_0: str_0}
    var_0 = module_0.topological_ordering(dict_0)
    str_1 = ""
    var_1 = module_0.topological_ordering(str_1)
    str_2 = "5JGB1cr ~9 pdr"
    str_3 = "kVDbu"
    dict_1 = {str_1: str_1, str_1: str_1, str_2: str_1, str_3: str_2}
    module_2.object(**dict_1)


def test_case_4():
    node_0 = module_1.Node()
    list_0 = [node_0, node_0]
    node_1 = module_1.Node(list_0, outgoing_nodes=list_0)
    dict_0 = {node_1: node_0, node_1: node_0}
    var_0 = module_0.topological_ordering(dict_0)