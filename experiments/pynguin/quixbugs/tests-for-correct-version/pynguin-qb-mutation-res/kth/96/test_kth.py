# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kth as module_0


def test_case_0():
    bool_0 = False
    dict_0 = {bool_0: bool_0}
    var_0 = module_0.kth(dict_0, bool_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.kth(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 1022
    int_1 = 754
    bool_0 = False
    dict_0 = {int_1: int_0, int_1: bool_0}
    tuple_0 = (int_0, int_1, dict_0)
    none_type_0 = None
    module_0.kth(tuple_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x83\xdf\xc9"
    set_0 = {bytes_0, bytes_0, bytes_0}
    module_0.kth(bytes_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    dict_0 = {bool_0: bool_0}
    var_0 = module_0.kth(dict_0, bool_0)
    assert var_0 is False
    bytes_0 = b"\xbe}WWj\xe2\xd9\xc9z\xbb\xed\x1dy\xb4F\x83\x88\xd5\x9a\xdf"
    bool_1 = True
    var_1 = module_0.kth(bytes_0, bool_1)
    assert var_1 == 70
    module_0.kth(var_0, var_0)