# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2378 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 2374
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    int_0 = -471
    set_0 = {bool_0, int_0, bool_0, int_0}
    var_0 = module_0.func(*set_0)
    bytes_0 = b":v\xf3\xfaEo\x86"
    list_0 = [bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()