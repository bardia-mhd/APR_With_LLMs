# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_964 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"I\x91\xcd\xbc"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xba\xec\x9d\x11f\xcb2=N"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b";\xc8\x04`\xf5\x16\xb5"
    var_0 = module_0.func(*bytes_0)
    module_0.func()