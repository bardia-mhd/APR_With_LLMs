# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0


def test_case_0():
    bool_0 = False
    dict_0 = {bool_0: bool_0}
    var_0 = module_0.lis(dict_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    bytes_0 = b"\xf2\xed\xf3"
    tuple_0 = (bool_0, bytes_0)
    module_0.lis(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    complex_0 = -2094.501177 + 1110.9723j
    module_0.lis(complex_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"e\xcb\x02\xc7Q\xc6Hh"
    var_0 = module_0.lis(bytes_0)
    assert var_0 == 3
    var_1 = module_0.lis(bytes_0)
    assert var_1 == 3
    module_0.lis(var_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xc5\xfa\x90\x91.\xd7\x91"
    var_0 = module_0.lis(bytes_0)
    assert var_0 == 3
    int_0 = -622
    module_0.lis(int_0)