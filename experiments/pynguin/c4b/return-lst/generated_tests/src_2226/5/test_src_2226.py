# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2226 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xf6,,SX-\x13\xa4"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x13\x14x\x810b"
    var_0 = module_0.func(*bytes_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xf6,,SX-\x13\xa4"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_1.object()
    bytes_1 = b"!\xe4=\xc2\xa2\x92UQ\xdc\x91"
    var_2 = module_0.func(*bytes_1)
    module_0.func()