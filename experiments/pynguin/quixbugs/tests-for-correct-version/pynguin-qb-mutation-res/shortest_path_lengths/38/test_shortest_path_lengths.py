# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_path_lengths as module_0
import node as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    module_0.shortest_path_lengths(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b""
    module_0.shortest_path_lengths(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    dict_0 = {}
    var_0 = module_0.shortest_path_lengths(bool_0, dict_0)
    module_0.shortest_path_lengths(var_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    dict_0 = {}
    var_0 = module_0.shortest_path_lengths(bool_0, dict_0)
    node_0 = module_1.Node(incoming_nodes=dict_0)
    node_0.successors()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    dict_0 = {}
    var_0 = module_0.shortest_path_lengths(bool_0, dict_0)
    int_0 = 99
    var_1 = module_0.shortest_path_lengths(int_0, dict_0)
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "collections.defaultdict"
    )
    assert len(var_1) == 9801
    var_0.successors()