# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_271 as module_0


def test_case_0():
    float_0 = 1115.484525
    dict_0 = {float_0: float_0}
    var_0 = module_0.func(*dict_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    float_0 = 1116.1054528916695
    dict_0 = {float_0: float_0}
    var_0 = module_0.func(*dict_0)