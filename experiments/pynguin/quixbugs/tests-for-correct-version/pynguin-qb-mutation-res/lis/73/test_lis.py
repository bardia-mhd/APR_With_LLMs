# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "Qfe"
    var_0 = module_0.lis(str_0)
    assert var_0 == 2
    var_1 = module_0.lis(str_0)
    assert var_1 == 2
    module_0.lis(var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    var_0 = module_0.lis(dict_0)
    assert var_0 == 0
    module_0.lis(var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.lis(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "9lo6bDaS]dt5&"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.lis(list_0)
    assert var_0 == 1
    bytes_0 = b"\x14;\x82\xfceO\x88\xc7z\x12XY\xe9\xbd\x8c\xad&\x83"
    float_0 = -691.9
    bool_0 = False
    tuple_0 = (bytes_0, float_0, bool_0)
    module_0.lis(tuple_0)