# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_516 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "8#"
    list_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "rzZtHDZ&\x0bGJXOCQ*oG@X"
    tuple_0 = ()
    list_0 = [str_0, tuple_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "?WoXE 2Yx<|{0#4H91-|"
    tuple_0 = ()
    list_0 = [str_0, tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_1.object()
    module_0.func()