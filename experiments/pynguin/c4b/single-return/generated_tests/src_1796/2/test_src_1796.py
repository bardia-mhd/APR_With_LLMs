# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1796 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xdajz\xe6@\xb0{\xb9 \xdbq\x0f^\xaf,"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 210
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"x\x05\xbf\x15\x88@ \xba\xc9"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 14
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b")\xb0\xa6"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 287
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    bytes_0 = b"\x91\x80\x02\xf7~\x9b\xc5;<\xb5\xbd\xe6"
    none_type_0 = None
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
    module_0.func(*none_type_0)