# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2133 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    module_0.func(*bool_0)


def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    bytes_0 = b"\xd3\xb5\xde;\xc9t"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 116
    module_0.func(*bool_0)