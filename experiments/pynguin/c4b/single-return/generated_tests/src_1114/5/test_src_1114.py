# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1114 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "qMkzE2"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "qMkzE2"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x85\xf0S\xb5A\xa8Li\x1a\x1d`\xa9\xa7\xa75\xa8}[\xb2["
    module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"G\xcc\x87\xb7\x81\x85S\x8f"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == b"g\xcc\x87\xb7\x81\x85s\x8f"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"lP9\xbaP\xdf"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == b"Lp9\xbap\xdf"
    object_0 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "qMkzE2"
    var_0 = module_0.func(*str_0)
    assert var_0 == "Q"
    list_0 = [str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == "qMkzE2"
    module_0.func()


def test_case_5():
    str_0 = "qMkzE2"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "qMkzE2"
    var_1 = module_0.func(*var_0)
    assert var_1 == "Q"
    var_2 = module_0.func(*var_1)
    assert var_2 == "q"