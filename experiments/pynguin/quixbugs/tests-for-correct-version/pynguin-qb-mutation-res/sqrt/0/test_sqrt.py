# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sqrt as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    int_0 = -4098
    module_0.sqrt(bool_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    var_0 = module_0.sqrt(bool_0, bool_0)
    assert var_0 == pytest.approx(0.5, abs=0.01, rel=0.01)
    tuple_0 = ()
    module_0.sqrt(tuple_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    module_0.sqrt(dict_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 652
    none_type_0 = None
    var_0 = module_0.sqrt(int_0, int_0)
    assert var_0 == pytest.approx(30.04391139710254, abs=0.01, rel=0.01)
    module_0.sqrt(int_0, none_type_0)