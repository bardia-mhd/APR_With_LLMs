# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import max_sublist_sum as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "_"
    module_0.max_sublist_sum(str_0)


def test_case_1():
    bytes_0 = b";\x9a"
    var_0 = module_0.max_sublist_sum(bytes_0)
    assert var_0 == 213


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 185
    module_0.max_sublist_sum(int_0)