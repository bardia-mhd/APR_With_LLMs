# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sieve as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1039
    var_0 = module_0.sieve(int_0)
    var_1 = module_0.sieve(int_0)
    module_0.sieve(var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    var_0 = module_0.sieve(bool_0)
    tuple_0 = (var_0, var_0)
    list_0 = [var_0]
    tuple_1 = (bool_0, tuple_0, list_0, list_0)
    str_0 = "D682n"
    list_1 = [tuple_1, tuple_0, tuple_1, str_0]
    bool_1 = False
    var_1 = module_0.sieve(bool_1)
    module_0.sieve(list_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "-lqyJ\n7QIXrgG\r#1S#`"
    module_0.sieve(str_0)