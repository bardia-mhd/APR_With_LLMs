# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import max_sublist_sum as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    complex_0 = 163.66818 + 493.87j
    list_0 = [complex_0, complex_0, complex_0, complex_0]
    module_0.max_sublist_sum(list_0)


def test_case_1():
    bytes_0 = b"\x1b\x8a\x16\x18>\x7fG"
    var_0 = module_0.max_sublist_sum(bytes_0)
    assert var_0 == 471
    var_1 = module_0.max_sublist_sum(bytes_0)
    assert var_1 == 471
    var_2 = module_0.max_sublist_sum(bytes_0)
    assert var_2 == 471