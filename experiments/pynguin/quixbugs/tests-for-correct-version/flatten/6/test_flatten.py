# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import flatten as module_0
import builtins as module_1


def test_case_0():
    none_type_0 = None
    var_0 = module_0.flatten(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xee\x89Pp"
    var_0 = module_0.flatten(bytes_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
    list_1 = [list_0]
    var_0 = module_0.flatten(list_1)
    bytes_0 = b"\xee\xb3"
    list_2 = [bytes_0, bytes_0, bytes_0]
    int_0 = -242
    tuple_0 = (bytes_0, list_2, int_0)
    var_1 = module_0.flatten(tuple_0)
    module_1.object(*var_1)