# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import hanoi as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    var_0 = module_0.hanoi(bool_0, bool_0)
    list_0 = [var_0, var_0, bool_0]
    int_0 = 2227
    tuple_0 = (list_0, int_0, var_0, bool_0)
    list_1 = [tuple_0]
    module_0.hanoi(list_1, list_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "]\x0b{?&3w2|S/;"
    module_0.hanoi(str_0)