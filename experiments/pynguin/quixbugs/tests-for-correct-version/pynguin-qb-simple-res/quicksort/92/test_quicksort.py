# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import quicksort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 54
    module_0.quicksort(int_0)


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.quicksort(tuple_0)
    var_1 = module_0.quicksort(tuple_0)


def test_case_2():
    bytes_0 = b"\xca\x0f\xd0 \xb2\x0321\t"
    var_0 = module_0.quicksort(bytes_0)
    bool_0 = False
    var_1 = module_0.quicksort(bool_0)
    var_2 = module_0.quicksort(bool_0)