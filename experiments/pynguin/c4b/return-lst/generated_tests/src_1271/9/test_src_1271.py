# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1271 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "8"
    bytes_0 = b"Dx\xee|\xbf"
    list_0 = [str_0, str_0, str_0, bytes_0]
    var_0 = module_0.func(*list_0)
    module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "8"
    bytes_0 = b"Dx\xee|\xbf"
    float_0 = -925.948
    list_0 = [float_0, str_0, bytes_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "8"
    bytes_0 = b""
    list_0 = [str_0, bytes_0, str_0, str_0, str_0, bytes_0]
    var_0 = module_0.func(*list_0)
    module_0.func()