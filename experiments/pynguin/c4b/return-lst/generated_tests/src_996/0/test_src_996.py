# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_996 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "y[I>}"
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    list_1 = [bool_0, list_0, bool_0]
    list_2 = [list_1, bool_0, bool_0, list_1]
    module_0.func(*list_2)