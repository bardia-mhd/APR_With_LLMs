# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1311 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"|\xa9cq\xca[6\x0b\x1av"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 5
    module_0.func()