# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import flatten as module_0
import builtins as module_1


def test_case_0():
    int_0 = -658
    var_0 = module_0.flatten(int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xf6\x95_H"
    var_0 = module_0.flatten(bytes_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xb9\xdb\xe1\xf6\x0c\xf1\xe4\xd3\xea+"
    int_0 = 2352
    list_0 = [int_0, bytes_0, int_0]
    bool_0 = True
    tuple_0 = (int_0, list_0, int_0, bool_0)
    var_0 = module_0.flatten(tuple_0)
    module_1.object(*var_0)