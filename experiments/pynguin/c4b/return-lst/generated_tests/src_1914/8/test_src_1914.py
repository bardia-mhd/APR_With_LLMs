# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1914 as module_0
import builtins as module_1


def test_case_0():
    str_0 = '7Jo$*">1oS\x0c$K~'
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_1():
    str_0 = "7J'oVV#X>1]oS\x0c;~"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_1 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


def test_case_3():
    str_0 = "]g!VWj2"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "7J'oVVKX>1]oS\x0c;K~"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


def test_case_5():
    str_0 = "7J'oVV#X>1]oS\x0c;~"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "fN#_KKf\n#"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "fN#VKKf\n#"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    object_0 = module_1.object()
    var_0 = module_0.func(*list_0)
    module_0.func()