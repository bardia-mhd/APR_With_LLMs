# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_in_sorted as module_0


def test_case_0():
    str_0 = '7U!"<\x0cW|z.MH8/pKH;2\n'
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    module_0.find_in_sorted(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "=\\X85AHq_}5"
    list_0 = [str_0]
    var_0 = module_0.find_in_sorted(list_0, str_0)
    assert var_0 == 0
    module_0.find_in_sorted(var_0, list_0)