# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2459 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b",\xd2H!\xc5<\x85\x14\xb8\xc3\x07"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"J\x04\xe1\xe1\xf8\x01"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_1.object()
    module_0.func()