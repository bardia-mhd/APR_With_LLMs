# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kth as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.kth(list_0, bool_0)
    assert var_0 is False
    module_0.kth(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xb2\xbe[I\xc4y\x7f\xa9\xf0\x8b\x98+"
    module_0.kth(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    str_0 = 'x5"a7,D:";"K\\Ac&@-}'
    var_0 = module_0.kth(str_0, bool_0)
    assert var_0 == '"'
    module_0.kth(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    str_0 = ">"
    module_0.kth(str_0, bool_0)