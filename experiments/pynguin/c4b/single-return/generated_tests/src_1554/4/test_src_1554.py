# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1554 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"#\xa66\xd1\xa0\x81\x9d\x1d\x83"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 3
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    bytes_0 = b"#\xa6q\xd1\xa0\x9d\x83\x12"
    var_1 = module_0.func(*bytes_0)
    assert var_1 == 3
    list_1 = [var_1, var_1]
    var_2 = module_0.func(*list_1)
    assert var_2 == 1
    module_0.func()