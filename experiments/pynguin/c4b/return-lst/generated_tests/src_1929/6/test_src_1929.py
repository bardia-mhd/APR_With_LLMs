# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1929 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"w\x93\x85\xff^\xa4\xc2\xf8"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "c2EQ$O.|K"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    str_0 = "X1(]$eK]"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_4():
    str_0 = 'z8*"$3\t@8:\t'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


def test_case_5():
    str_0 = "a26cZ\x0brjq5 >|\x0cziI7"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_6():
    str_0 = "h4U+"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_7():
    str_0 = "a1(]$eK]"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_8():
    int_0 = 679
    list_0 = [int_0, int_0, int_0]
    list_1 = [list_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
    str_0 = "h17U+"
    var_1 = module_0.func(*list_1)
    list_2 = [str_0, str_0]
    var_2 = module_0.func(*list_2)
    object_0 = module_1.object()
    object_1 = module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = "h87U+"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_10():
    int_0 = 16
    list_0 = [int_0, int_0, int_0, int_0]
    list_1 = [list_0, list_0, list_0, int_0]
    var_0 = module_0.func(*list_1)
    str_0 = "a8cZ\x0bjq5 >|\t\x0cziI7"
    list_2 = [str_0, var_0, str_0, str_0, list_0, str_0]
    var_1 = module_0.func(*list_2)
    module_1.object(*list_2)