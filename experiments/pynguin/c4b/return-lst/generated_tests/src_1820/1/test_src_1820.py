# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1820 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "3"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.func(*none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "4W"
    var_0 = module_0.func(*str_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x12\x8c\xf8"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xb6\x9d\x10\x95\x9ac<{\xdf\x8e\xc4\xf9\xcb\xc0\xc9\xad\xe9?\xe6"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*bytes_0)
    module_0.func()