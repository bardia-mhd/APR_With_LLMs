# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1139 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -3014.615108
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xee=\xd6\xafq\xee\xd9P\x93\xf0\x1f"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\r\xea\xa0\x9b\xfd%\x12\x13"
    var_0 = module_0.func(*bytes_0)
    list_0 = [var_0, var_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x14\xf9L\xd9\x01zAH+7H\x8d\x93\xb1\x0fR\xa6\xd5"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*var_0)
    module_0.func()