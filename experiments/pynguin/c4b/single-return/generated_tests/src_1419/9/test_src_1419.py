# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1419 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    set_0 = set()
    list_0 = [set_0, none_type_0, none_type_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "e5\r5fs9#}6[;"
    var_0 = module_0.func(*str_0)
    assert var_0 == "E"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "\t=Y^ ^"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "=y^^"
    none_type_0 = None
    module_0.func(*none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "nHe#|G6^0ef/d"
    var_0 = module_0.func(*str_0)
    assert var_0 == "N"
    var_1 = module_0.func(*var_0)
    assert var_1 == "n"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "nHe#|G6^0ef/d"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "nHe#|G6^0ef/d"
    none_type_0 = None
    module_0.func(*none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "\t=Y^ n"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "=Y^n"
    module_0.func(*str_0)