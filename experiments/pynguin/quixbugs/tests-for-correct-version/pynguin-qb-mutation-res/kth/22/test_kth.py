# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kth as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x92X\xb6\xd8\xe3\xd3\xc3\x8e\x11O"
    module_0.kth(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.kth(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -375
    list_0 = [int_0]
    module_0.kth(list_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 2687
    list_0 = [int_0]
    module_0.kth(list_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xe6\x07\xe0\xf7z\x11\xe8|-\x89\xe7\xdf"
    bool_0 = False
    var_0 = module_0.kth(bytes_0, bool_0)
    assert var_0 == 7
    var_1 = module_0.kth(bytes_0, bool_0)
    assert var_1 == 7
    bytes_1 = b"P\x909\xf2C\xd3\xcf\n*"
    float_0 = -2547.0
    module_0.kth(bytes_1, float_0)