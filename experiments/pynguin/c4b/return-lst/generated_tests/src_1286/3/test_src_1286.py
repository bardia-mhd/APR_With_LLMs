# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1286 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"\xcb\xa7\x0f4\x9d\xe6\xe8C\xdc\xa6\x1bJD"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    list_1 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_2 = module_0.func(*list_1)
    object_0 = module_1.object()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xcb\xa7\x0f4\x9d\xe6\xe8C\xdc\xa6\x1bJD"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    list_1 = [bytes_0, bytes_0, bytes_0]
    var_2 = module_0.func(*list_1)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xcb\xa7\x0f4\x9d\xe6\xe8C\xdc\xa6\x1bJD"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    list_1 = [bytes_0, bytes_0]
    var_1 = module_0.func(*list_1)
    list_2 = [bytes_0, bytes_0]
    var_2 = module_0.func(*list_2)
    var_3 = module_0.func(*var_1)
    list_3 = [var_0, bytes_0, var_0, list_2, bytes_0, bytes_0, bytes_0]
    var_4 = module_0.func(*list_3)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0]
    list_1 = [list_0, none_type_0]
    var_0 = module_0.func(*list_1)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\xcb\xa7\x0f4\xe6\xe8C\xdc\xa6\x1bJD"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    bytes_0 = b"\xcb\xa7\x0f4\x9d\xe6\xe8C\xdc\xa6\x1bJD"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    list_1 = [bytes_0, bytes_0]
    var_1 = module_0.func(*list_1)
    list_2 = [bytes_0, bytes_0]
    var_2 = module_0.func(*list_2)
    var_3 = module_0.func(*var_1)
    var_4 = module_0.func(*var_3)
    list_3 = [var_2]
    module_1.object(*list_3)