# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1299 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"0"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 7
    module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"5"
    list_0 = [
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
    ]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    module_1.object(**bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = '8187/Wd^e1t"'
    module_0.func(*str_0)