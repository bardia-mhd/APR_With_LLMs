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
    bytes_0 = b"H\xc7\x82t_,\xcc\xa8\xfb"
    var_0 = module_0.flatten(bytes_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"lq\x7f\x9c\xc1\xdc\xa3"
    var_0 = module_0.flatten(bytes_0)
    int_0 = 673
    list_0 = [int_0]
    bool_0 = True
    tuple_0 = (list_0, var_0, var_0, bool_0)
    var_1 = module_0.flatten(tuple_0)
    module_1.object(*var_1)