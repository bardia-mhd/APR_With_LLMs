# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_996 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = ")guL"
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    list_0 = [set_0, set_0, set_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.func(*none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"->\x87\xac\xc5eR\xe0\t7c\x8b\x87\xa4\x86\xa5"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "-H\r1*P"
    str_1 = "@WK(p\r'uO}aURF,Hhs/i"
    bool_0 = False
    tuple_0 = (str_0, str_1, bool_0)
    module_0.func(*tuple_0)