# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import wrap as module_0


def test_case_0():
    str_0 = "W;j)v2\\,/q\tez:"
    bool_0 = True
    var_0 = module_0.wrap(str_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    tuple_0 = ()
    var_0 = module_0.wrap(tuple_0, bool_0)
    module_0.wrap(var_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"t^$}n\xbd\xe3Ft\xfb"
    module_0.wrap(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "n "
    bool_0 = True
    var_0 = module_0.wrap(str_0, bool_0)
    float_0 = -2838.9851
    module_0.wrap(float_0, var_0)