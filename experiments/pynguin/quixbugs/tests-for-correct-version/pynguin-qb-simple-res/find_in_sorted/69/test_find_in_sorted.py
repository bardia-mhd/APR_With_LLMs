# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_in_sorted as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "q]ly=p-`:?"
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1
    module_0.find_in_sorted(str_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"ECr\x7f\xf0u\xa3\xc7\xa1+N^>\xdch\x10\x17\x91"
    none_type_0 = None
    module_0.find_in_sorted(bytes_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.find_in_sorted(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "PG'q\r{.o`\"Hs"
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1
    module_0.find_in_sorted(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    dict_0 = {bool_0: bool_0}
    var_0 = module_0.find_in_sorted(dict_0, bool_0)
    assert var_0 == 0
    var_1 = module_0.find_in_sorted(dict_0, bool_0)
    assert var_1 == 0
    module_0.find_in_sorted(bool_0, var_0)