# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_paths as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x9ffl\xdf\xbb"
    module_0.shortest_paths(bytes_0, bytes_0)


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.shortest_paths(tuple_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    tuple_0 = ()
    tuple_1 = (tuple_0, tuple_0)
    var_0 = module_0.shortest_paths(tuple_1, tuple_0)
    var_1 = module_0.shortest_paths(none_type_0, var_0)
    complex_0 = -1349.406981 + 231.11j
    bytes_0 = b"\x11\x05\xf5\xea\xae\x86kDp\x9d\xfd\xe1\xd4\xb8N\x93\x10 \x98"
    tuple_2 = (var_1, complex_0, bytes_0)
    module_0.shortest_paths(tuple_2, complex_0)