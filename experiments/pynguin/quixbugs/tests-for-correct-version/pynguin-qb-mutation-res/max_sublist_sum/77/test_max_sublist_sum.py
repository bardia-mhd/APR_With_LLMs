# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import max_sublist_sum as module_0


def test_case_0():
    int_0 = 501
    list_0 = [int_0]
    var_0 = module_0.max_sublist_sum(list_0)
    assert var_0 == 501


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    module_0.max_sublist_sum(bool_0)