# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2371 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "_!3v|[p)OKhd[%E"
    bytes_0 = b"0W@H\x12mMT"
    list_0 = [str_0, str_0, str_0, bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = ";6UQ;K#rk>!T?t*o"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_1.object(*list_0)