# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_711 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"O\xf4\xdd=\xbcz\xd0\x97O\xe3\x91(\xc1\x1d\x9a\xd4{\xf9y"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()