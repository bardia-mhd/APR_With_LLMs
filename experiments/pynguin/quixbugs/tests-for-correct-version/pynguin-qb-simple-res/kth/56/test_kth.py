# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kth as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "(iJSa=)H89*N'l"
    int_0 = 760
    module_0.kth(str_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x08@\xa1\xbd\xfb\x93\xa2\x17\x1dLV\xe5a\x8a\xd5\xb6D\x00Y"
    module_0.kth(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    set_0 = set()
    module_0.kth(set_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "(iJSa=)H89CNPl"
    object_0 = module_1.object()
    int_0 = -998
    module_0.kth(str_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.kth(list_0, bool_0)
    assert var_0 is True
    var_1 = module_0.kth(list_0, bool_0)
    assert var_1 is True
    float_0 = 274.24438
    module_0.kth(list_0, float_0)