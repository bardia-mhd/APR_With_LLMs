# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_657 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "618"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_2():
    str_0 = "60"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "618"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "18"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*list_0)
    module_1.object(*str_0, **var_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "6189"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "6170"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_1.object(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "6178"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_1.object(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "28"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = "618"
    bytes_0 = b"\x82\xf4\x87\xb8&[\x1e\x024G]\xd4\x08\x18\xae+\x00\xc6B"
    list_0 = [str_0, bytes_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    var_2 = module_0.func(*list_0)
    module_0.func(*var_1)


@pytest.mark.xfail(strict=True)
def test_case_10():
    str_0 = "618"
    bytes_0 = b"\x82\xf4\x87\x03&[4G]\xd4\x08\x18\xaeD+\x00\x9aB"
    list_0 = [str_0, bytes_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    var_2 = module_0.func(*str_0)
    module_0.func(*var_2)