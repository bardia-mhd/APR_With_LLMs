# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1295 as module_0


def test_case_0():
    str_0 = "k;1+G*-YN6]:*|\x0cpK"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = ".i4QBINC]-Y"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "YES"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "9"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "YES"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "53gck(Hs.<-H%Mx49"
    bool_0 = True
    list_0 = []
    tuple_0 = (bool_0, list_0, bool_0)
    dict_0 = {str_0: tuple_0, str_0: list_0, str_0: str_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == "YES"
    module_0.func()