# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_in_sorted as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "tW"
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1
    bytes_0 = b"\x96\xe0\xc6\xf4"
    set_0 = {bytes_0, bytes_0}
    module_0.find_in_sorted(set_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"A7f\xa9;\x01;\x9eN\xdax\xf6"
    none_type_0 = None
    module_0.find_in_sorted(bytes_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.find_in_sorted(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "8<]Y"
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1
    str_1 = "]_"
    none_type_0 = None
    module_0.find_in_sorted(str_1, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 1129
    set_0 = {int_0}
    list_0 = [set_0, int_0]
    var_0 = module_0.find_in_sorted(list_0, int_0)
    assert var_0 == 1
    module_0.find_in_sorted(set_0, list_0)