# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1016 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -4912.902097
    bool_0 = True
    tuple_0 = ()
    tuple_1 = (float_0, bool_0, tuple_0)
    var_0 = module_0.func(*tuple_1)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xcd\xc4\x06<\x02{\xb2H\xe4\xd0\t\xe6y\xf9`,\xbb\xd0~s"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()