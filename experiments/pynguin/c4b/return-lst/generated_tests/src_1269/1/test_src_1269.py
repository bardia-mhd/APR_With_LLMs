# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1269 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    bool_0 = False
    bytes_0 = b"[M|\xc7\xd6\x7f\x92T\xb48&\xc7Y\xc6\xd9\xa9U"
    list_0 = [bool_0, bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    bytes_0 = b"\x06M|\xc7\xd6\xc3\x7f\x92T\xb48\x08\xc7Y\xc6\xd9\xd0U"
    list_0 = [bool_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "33]eC=JXJ}"
    var_0 = module_0.func(*str_0)
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "95Rvw!$TpNolnp:6"
    module_0.func(*str_0)