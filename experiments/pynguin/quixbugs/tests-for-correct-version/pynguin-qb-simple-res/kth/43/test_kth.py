# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kth as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 2233
    bytes_0 = b"\x9b\x1bK\xf9{-"
    tuple_0 = (int_0, bytes_0)
    module_0.kth(tuple_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    none_type_0 = None
    module_0.kth(list_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    complex_0 = -3103.127201 - 2716.67414j
    module_0.kth(complex_0, complex_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ">Out2\"wHO{'_bXZ6"
    module_0.kth(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.kth(list_0, bool_0)
    assert var_0 is False
    var_1 = module_1.object()
    bytes_0 = b"\xfa\xe5\xc1~\xdf\x197\xe2\x10"
    module_0.kth(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = ">Out2\"wHO{'_bXZ6"
    float_0 = 4202.0
    module_0.kth(str_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = ">Out2\"wHO{'_bXZ6"
    int_0 = -1203
    module_0.kth(str_0, int_0)