# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import minimum_spanning_tree as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    tuple_0 = ()
    var_0 = module_0.minimum_spanning_tree(tuple_0)
    dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0}
    module_0.minimum_spanning_tree(dict_0)


def test_case_1():
    list_0 = []
    var_0 = module_0.minimum_spanning_tree(list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"sF\x89\xff,\xd8D\xc2"
    module_0.minimum_spanning_tree(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x013"
    dict_0 = {bytes_0: bytes_0}
    var_0 = module_0.minimum_spanning_tree(dict_0)
    tuple_0 = ()
    var_1 = module_0.minimum_spanning_tree(tuple_0)
    dict_1 = {tuple_0: var_1, tuple_0: var_1, tuple_0: tuple_0, tuple_0: var_1}
    module_0.minimum_spanning_tree(dict_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    tuple_0 = (bool_0, bool_0)
    dict_0 = {tuple_0: tuple_0}
    var_0 = module_0.minimum_spanning_tree(dict_0)
    object_0 = module_1.object(*var_0)
    module_0.minimum_spanning_tree(object_0)