# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import quicksort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    complex_0 = -202.5 - 23.256j
    module_0.quicksort(complex_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.quicksort(none_type_0)
    var_1 = module_0.quicksort(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"p:,\xd5"
    dict_0 = {}
    tuple_0 = ()
    tuple_1 = (bytes_0, dict_0, tuple_0)
    module_0.quicksort(tuple_1)


def test_case_3():
    bytes_0 = b"\xd2U\x80"
    none_type_0 = None
    var_0 = module_0.quicksort(none_type_0)
    var_1 = module_0.quicksort(bytes_0)
    var_2 = module_0.quicksort(var_1)
    bool_0 = False
    var_3 = module_0.quicksort(bool_0)
    var_4 = module_0.quicksort(bool_0)