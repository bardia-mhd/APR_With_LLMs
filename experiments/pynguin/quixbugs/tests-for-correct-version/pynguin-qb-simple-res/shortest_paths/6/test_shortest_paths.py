# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_paths as module_0


def test_case_0():
    tuple_0 = ()
    var_0 = module_0.shortest_paths(tuple_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 4587
    bool_0 = False
    set_0 = {int_0, int_0, bool_0}
    module_0.shortest_paths(set_0, set_0)


def test_case_2():
    bool_0 = True
    tuple_0 = (bool_0, bool_0)
    dict_0 = {tuple_0: tuple_0, tuple_0: bool_0}
    var_0 = module_0.shortest_paths(tuple_0, dict_0)
    tuple_1 = ()
    var_1 = module_0.shortest_paths(tuple_1, tuple_1)