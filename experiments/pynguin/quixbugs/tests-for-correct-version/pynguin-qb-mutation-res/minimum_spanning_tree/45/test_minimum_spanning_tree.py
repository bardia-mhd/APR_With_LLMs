# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import minimum_spanning_tree as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    module_0.minimum_spanning_tree(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b""
    var_0 = module_0.minimum_spanning_tree(bytes_0)
    var_1 = module_0.minimum_spanning_tree(bytes_0)
    module_0.minimum_spanning_tree(var_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 279
    tuple_0 = (int_0, int_0)
    dict_0 = {tuple_0: int_0, tuple_0: int_0}
    var_0 = module_0.minimum_spanning_tree(dict_0)
    module_0.minimum_spanning_tree(int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x06,"
    dict_0 = {bytes_0: bytes_0}
    var_0 = module_0.minimum_spanning_tree(dict_0)
    var_0.successor()