# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1179 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xda\xf5\xe7l\x8e\t\xd3+e"
    var_0 = module_0.func(*bytes_0)
    bool_0 = True
    module_0.func(*bool_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xda\x9b\xf5\xe7l\x8e\t\xd3+e"
    var_0 = module_0.func(*bytes_0)
    bool_0 = True
    module_0.func(*bool_0)