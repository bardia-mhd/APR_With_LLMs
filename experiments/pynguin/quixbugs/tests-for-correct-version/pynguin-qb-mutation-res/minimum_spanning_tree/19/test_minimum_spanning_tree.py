# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import minimum_spanning_tree as module_0


def test_case_0():
    bytes_0 = b">q"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    var_0 = module_0.minimum_spanning_tree(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "IJ+ZzuCP`I <j"
    module_0.minimum_spanning_tree(str_0)


def test_case_2():
    bytes_0 = b"ZZ"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
    var_0 = module_0.minimum_spanning_tree(dict_0)