# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import max_sublist_sum as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "G\x0bqtG#`K\rR[[iMy"
    module_0.max_sublist_sum(str_0)


def test_case_1():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.max_sublist_sum(dict_0)
    assert var_0 == 0
    var_1 = module_0.max_sublist_sum(dict_0)
    assert var_1 == 0
    var_2 = module_0.max_sublist_sum(dict_0)
    assert var_2 == 0