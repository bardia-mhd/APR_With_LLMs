# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kth as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 100
    str_0 = "S1[#cq&I\\WZ\x0bxY\r\x0ch\tF\\"
    module_0.kth(str_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.kth(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -402
    str_0 = "S1[#cq&I\\WZ\x0bxY\r\x0ch\tFX"
    module_0.kth(str_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 9
    str_0 = "S91[#cq&\\WZ\x0bY\r{h\tF\\"
    var_0 = module_0.kth(str_0, int_0)
    assert var_0 == "W"
    module_0.kth(int_0, str_0)