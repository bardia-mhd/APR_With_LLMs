# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0


def test_case_0():
    float_0 = 619.2
    dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0, float_0: float_0}
    var_0 = module_0.lis(dict_0)
    assert var_0 == 1


def test_case_1():
    str_0 = "lrdufj-g97&CsX1o"
    var_0 = module_0.lis(str_0)
    assert var_0 == 5
    str_1 = "'zfD"
    var_1 = module_0.lis(str_1)
    assert var_1 == 2


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -118.814087
    module_0.lis(float_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 1828.34
    str_0 = " -@"
    list_0 = [float_0, float_0, float_0, str_0]
    module_0.lis(list_0)