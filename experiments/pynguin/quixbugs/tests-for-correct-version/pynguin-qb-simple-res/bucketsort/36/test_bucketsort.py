# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bucketsort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 652
    int_1 = 1691
    tuple_0 = (int_0, int_1)
    module_0.bucketsort(tuple_0, int_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xe7"
    module_0.bucketsort(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 652
    int_1 = 1698
    tuple_0 = (int_0, int_0)
    var_0 = module_0.bucketsort(tuple_0, int_1)
    module_0.bucketsort(int_0, int_0)