# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import to_base as module_0
import collections as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1998
    var_0 = module_0.to_base(int_0, int_0)
    assert var_0 == "10"
    str_0 = "zsPu\x0c\nnd\x0c7b`3F<8DQ"
    module_0.to_base(str_0, int_0)


def test_case_1():
    chain_map_0 = module_1.ChainMap()
    var_0 = chain_map_0.__bool__()
    var_1 = module_0.to_base(var_0, var_0)
    assert var_1 == ""


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.to_base(none_type_0, none_type_0)