# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2128 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -1728
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b'K\xe3\xff\xeb\xe2"\xe5\x1d\\\xec\xf8x\xd8\xac\x97F\x1c\x97\xfc\xd5'
    var_0 = module_0.func(*bytes_0)
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


def test_case_3():
    int_0 = 1940
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)