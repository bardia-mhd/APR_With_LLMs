# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import next_palindrome as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "b"
    module_0.next_palindrome(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    var_0 = module_0.next_palindrome(list_0)
    module_1.object(*list_0, **list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.next_palindrome(bool_0)


def test_case_3():
    list_0 = []
    var_0 = module_0.next_palindrome(list_0)
    object_0 = module_0.next_palindrome(var_0)


def test_case_4():
    list_0 = []
    var_0 = module_0.next_palindrome(list_0)
    var_1 = module_0.next_palindrome(var_0)
    var_2 = module_0.next_palindrome(var_0)
    var_3 = module_0.next_palindrome(var_1)
    var_4 = module_0.next_palindrome(var_1)
    var_5 = module_0.next_palindrome(var_0)
    var_6 = module_0.next_palindrome(var_1)
    var_7 = module_0.next_palindrome(var_2)
    var_8 = module_0.next_palindrome(var_0)
    var_9 = module_0.next_palindrome(var_7)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "KV-Ic4/"
    bool_0 = False
    list_0 = [str_0, str_0, bool_0, str_0, str_0]
    var_0 = module_0.next_palindrome(list_0)
    module_0.next_palindrome(bool_0)