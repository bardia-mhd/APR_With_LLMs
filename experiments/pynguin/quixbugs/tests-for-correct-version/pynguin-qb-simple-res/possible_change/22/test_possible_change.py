# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0


def test_case_0():
    dict_0 = {}
    list_0 = [dict_0, dict_0, dict_0]
    bool_0 = False
    var_0 = module_0.possible_change(list_0, bool_0)
    assert var_0 == 1
    bool_1 = False
    bool_2 = True
    list_1 = [bool_1, bool_1, bool_1, bool_2]
    var_1 = module_0.possible_change(bool_1, bool_2)
    assert var_1 == 0
    var_2 = module_0.possible_change(list_1, bool_1)
    assert var_2 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x86\xacQU\xa4$}5t>\xed\x1d"
    module_0.possible_change(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -900
    bool_0 = True
    int_1 = -1716
    var_0 = module_0.possible_change(int_1, int_0)
    assert var_0 == 0
    module_0.possible_change(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 51
    none_type_0 = None
    var_0 = module_0.possible_change(none_type_0, int_0)
    assert var_0 == 0
    none_type_1 = None
    var_1 = module_0.possible_change(none_type_1, int_0)
    assert var_1 == 0
    bool_0 = True
    tuple_0 = (int_0, bool_0)
    module_0.possible_change(tuple_0, tuple_0)