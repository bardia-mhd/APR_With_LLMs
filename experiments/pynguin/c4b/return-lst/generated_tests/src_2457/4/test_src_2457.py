# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2457 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"%e%\x99f\xe6A"
    var_0 = module_0.func(*bytes_0)
    list_0 = [var_0]
    module_0.func(*list_0)