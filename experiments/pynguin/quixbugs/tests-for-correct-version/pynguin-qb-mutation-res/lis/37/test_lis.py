# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "t/.n7sH"
    var_0 = module_0.lis(str_0)
    assert var_0 == 3
    bool_0 = True
    module_0.lis(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_1.object(**none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    bytes_0 = b"\xb4\xd0\xe2\xc2\xbdY\xb4\xfaU\xd9\xbb\x1aT"
    var_0 = module_0.lis(bytes_0)
    assert var_0 == 4
    bool_1 = True
    str_0 = "[9bKnZ<("
    tuple_0 = (bool_0, bool_1, str_0)
    module_0.lis(tuple_0)