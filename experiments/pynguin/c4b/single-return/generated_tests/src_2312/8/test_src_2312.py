# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2312 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xb3\xad[\xc2\xf8\xe8*"
    list_0 = [bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "wn1%{<X4"
    var_0 = module_0.func(*str_0)
    assert var_0 == ".w"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b'>z\xbc\x17\x9e\xa4M\xcc\xdbJL"\xa1\x05\xa2A.\xcd'
    object_0 = module_1.object()
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    tuple_0 = (bytes_0, list_0)
    list_1 = [tuple_0, list_0, bytes_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "+[ps. QX#WyT?]j\nk?0"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".+.[.p.s... .q.x.#.w.t.?.].j.\n.k.?.0"
    var_1 = module_0.func(*str_0)
    assert var_1 == ".+"
    var_2 = module_1.object()
    module_0.func()