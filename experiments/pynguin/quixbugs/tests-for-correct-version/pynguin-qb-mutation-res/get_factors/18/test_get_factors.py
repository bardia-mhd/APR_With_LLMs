# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import get_factors as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    var_0 = module_0.get_factors(bool_0)
    bytes_0 = b"-\x12\xab7\xad\t\xc8"
    module_0.get_factors(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    object_0 = module_1.object()
    module_0.get_factors(object_0)


def test_case_2():
    int_0 = 2545
    var_0 = module_0.get_factors(int_0)


def test_case_3():
    bool_0 = False
    var_0 = module_0.get_factors(bool_0)