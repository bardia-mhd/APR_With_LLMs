# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1585 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"{\xc1\xec\x11:4\xc2\x89\xde\x90\xdf}\xf5\xdb\x93\x98"
    var_0 = module_0.func(*bytes_0)
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xb5\x154\xc7\x105\xac0"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x80I\xa5\xc1\x9c\x02\x83\x81U\x8f\x0f\xec\x98E"
    var_0 = module_0.func(*bytes_0)
    module_0.func()