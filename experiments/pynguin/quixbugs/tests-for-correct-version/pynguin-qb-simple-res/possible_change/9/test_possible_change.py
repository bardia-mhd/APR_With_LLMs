# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0


def test_case_0():
    bool_0 = False
    var_0 = module_0.possible_change(bool_0, bool_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0]
    module_0.possible_change(list_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -4680
    var_0 = module_0.possible_change(int_0, int_0)
    assert var_0 == 0
    bytes_0 = b"\xea\x9a\x91\x11\xe9\xcc\n\x9e\x92\xb1#\xdf7E'm\xce'\x12\xa0"
    module_0.possible_change(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 704.59212
    module_0.possible_change(float_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    var_0 = module_0.possible_change(bool_0, bool_0)
    assert var_0 == 1
    var_1 = module_0.possible_change(bool_0, bool_0)
    assert var_1 == 1
    bytes_0 = b"\x04x\xa5\x00\\\xddK\xe9\xdd\xf9\xf9\xcd\xae\x08Z\x01"
    var_2 = module_0.possible_change(bool_0, var_1)
    assert var_2 == 0
    none_type_0 = None
    module_0.possible_change(none_type_0, bytes_0)