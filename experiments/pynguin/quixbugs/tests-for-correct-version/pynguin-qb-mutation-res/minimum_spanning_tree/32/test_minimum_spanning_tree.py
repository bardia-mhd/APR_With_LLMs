# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import minimum_spanning_tree as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    dict_0 = {}
    bool_0 = False
    tuple_0 = (bool_0, bool_0)
    var_0 = module_0.minimum_spanning_tree(dict_0)
    module_0.minimum_spanning_tree(tuple_0)


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.minimum_spanning_tree(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xa8\xdc%@"
    module_0.minimum_spanning_tree(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\n\xb3"
    bytes_1 = b"\xc5\xbd\xde\xb4\x11\x03\x1c\x8d\x8a\xab\x8e\xeaW\x9e\xd3\x1b\xa3"
    dict_0 = {bytes_0: bytes_1, bytes_0: bytes_1, bytes_1: bytes_1}
    module_0.minimum_spanning_tree(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    dict_0 = {}
    bool_0 = False
    tuple_0 = (bool_0, bool_0)
    dict_1 = {tuple_0: bool_0}
    var_0 = module_0.minimum_spanning_tree(dict_1)
    var_1 = module_0.minimum_spanning_tree(dict_0)
    module_0.minimum_spanning_tree(tuple_0)