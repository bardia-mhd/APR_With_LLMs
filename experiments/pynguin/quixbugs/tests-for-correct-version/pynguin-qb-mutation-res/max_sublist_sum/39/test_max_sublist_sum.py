# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import max_sublist_sum as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    set_0 = set()
    bool_1 = True
    tuple_0 = (bool_0, bool_0, set_0, bool_1)
    tuple_1 = (tuple_0,)
    module_0.max_sublist_sum(tuple_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xd4\x83\xbf"
    var_0 = module_0.max_sublist_sum(bytes_0)
    assert var_0 == 534
    var_1 = module_0.max_sublist_sum(bytes_0)
    assert var_1 == 534
    bool_0 = False
    module_0.max_sublist_sum(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    complex_0 = -1231.52456 + 902.9201j
    module_0.max_sublist_sum(complex_0)