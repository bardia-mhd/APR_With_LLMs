# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import flatten as module_0
import builtins as module_1


def test_case_0():
    bool_0 = False
    var_0 = module_0.flatten(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"(\xe3\xa6p"
    var_0 = module_0.flatten(bytes_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x12\xec\xafg\x8d\xca\x15uY\x82\xe4?l@\xbf"
    list_0 = []
    tuple_0 = ()
    var_0 = module_0.flatten(list_0)
    complex_0 = 709.76437 - 922.3j
    tuple_1 = (tuple_0, bytes_0, complex_0)
    list_1 = [tuple_0, complex_0, tuple_1]
    tuple_2 = (list_0, tuple_1, list_1, complex_0)
    var_1 = module_0.flatten(tuple_2)
    module_1.object(*var_1)