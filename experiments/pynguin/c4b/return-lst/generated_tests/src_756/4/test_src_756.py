# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_756 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    str_0 = "Py0jP\nE~P"
    bytes_0 = b"\xa3\x8d\xe2Y\x1b\x81\x90?ghg\x1b\xa5\xb8"
    tuple_0 = (bool_0, bool_0, str_0, bytes_0)
    module_0.func(*tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    bool_1 = True
    list_1 = [var_0, bool_1]
    module_0.func(*list_1)