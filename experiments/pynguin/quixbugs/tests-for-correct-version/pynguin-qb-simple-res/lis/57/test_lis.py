# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0


def test_case_0():
    str_0 = "^ov$GD"
    dict_0 = {str_0: str_0}
    var_0 = module_0.lis(dict_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -1712.3101
    bool_0 = True
    int_0 = -1724
    tuple_0 = ()
    tuple_1 = (float_0, bool_0, int_0, tuple_0)
    list_0 = []
    str_0 = "R[\nn!s"
    tuple_2 = (tuple_1, bool_0, list_0, str_0)
    module_0.lis(tuple_2)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.lis(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xaa\xedv\x1a\x1ak\r\x8ew6\x94\xbd\xb5oi\x9d\xc3~\xcd"
    var_0 = module_0.lis(bytes_0)
    assert var_0 == 7
    none_type_0 = None
    module_0.lis(none_type_0)