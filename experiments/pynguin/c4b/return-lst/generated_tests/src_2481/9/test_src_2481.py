# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2481 as module_0


def test_case_0():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.func(*dict_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xb4\xe2\x901\x95h\x12\xdb\xb01\xd9b.\x0bdY"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x02\xcc\x9e}\xa9}w\x13\xfa\r/\xb6\x81?"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*bytes_0)
    module_0.func()