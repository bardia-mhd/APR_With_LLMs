# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import wrap as module_0


def test_case_0():
    int_0 = 487
    bytes_0 = b""
    list_0 = [int_0, bytes_0, int_0]
    var_0 = module_0.wrap(list_0, int_0)
    var_1 = module_0.wrap(bytes_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    module_0.wrap(bool_0, bool_0)


def test_case_2():
    str_0 = "mpf8t$'"
    bool_0 = True
    var_0 = module_0.wrap(str_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "#iLQ]cF "
    bool_0 = True
    var_0 = module_0.wrap(str_0, bool_0)
    module_0.wrap(str_0, str_0)