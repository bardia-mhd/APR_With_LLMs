# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_in_sorted as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    tuple_0 = ()
    var_0 = module_0.find_in_sorted(tuple_0, tuple_0)
    assert var_0 == -1
    module_0.find_in_sorted(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"&\xeb\n\xd83\x1a"
    module_0.find_in_sorted(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.find_in_sorted(none_type_0, none_type_0)


def test_case_3():
    str_0 = "A\t/jNR9*w\t[mT"
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "_g~qMKu~-.S+9"
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1
    list_0 = [var_0, var_0, var_0, var_0]
    var_1 = module_0.find_in_sorted(list_0, var_0)
    assert var_1 == 2
    var_2 = module_0.find_in_sorted(list_0, var_1)
    assert var_2 == -1
    module_0.find_in_sorted(var_0, var_1)