# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2079 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    bytes_0 = b"\x19 g'Q "
    list_0 = [bool_0, bool_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 630
    bool_0 = False
    list_0 = [int_0, int_0, bool_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x19 g'Q "
    var_0 = module_0.func(*bytes_0)
    module_0.func()