# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import max_sublist_sum as module_0


def test_case_0():
    bytes_0 = b"c"
    var_0 = module_0.max_sublist_sum(bytes_0)
    assert var_0 == 99


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -1934
    module_0.max_sublist_sum(int_0)