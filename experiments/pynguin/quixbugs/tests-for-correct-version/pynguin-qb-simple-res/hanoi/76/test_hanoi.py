# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import hanoi as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1967
    module_0.hanoi(int_0, int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    var_0 = module_0.hanoi(bool_0)
    str_0 = 'gP3G<";P'
    bool_1 = False
    list_0 = [str_0, bool_1]
    module_0.hanoi(list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    set_0 = set()
    list_0 = [set_0]
    module_0.hanoi(list_0)