# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_557 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"\x91\x99n|p@E\x13e\xe3`\xff\xa6"
    tuple_0 = (bytes_0,)
    list_0 = [tuple_0, bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "&iPF-E\rymooWj_=-H"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, str_0, str_0, str_0]
    var_1 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "ks]i9Rm6)g^a_l"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, str_0, str_0, str_0]
    var_1 = module_0.func(*list_0)
    var_2 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "@`3<<(Q"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, str_0, str_0, str_0]
    var_1 = module_0.func(*list_0)
    var_2 = module_1.object()
    module_0.func()