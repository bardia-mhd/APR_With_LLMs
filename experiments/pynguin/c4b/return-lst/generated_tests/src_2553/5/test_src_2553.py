# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2553 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xcc\x9a\x17\xa4.p*\x8d\xacK8uqQw\xb5y"
    var_0 = module_0.func(*bytes_0)
    module_1.object(*var_0, **var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    bytes_0 = b"\x85\xd9z>J\xcd\x1c\xe8@\xd4"
    var_1 = module_0.func(*bytes_0)
    module_0.func()