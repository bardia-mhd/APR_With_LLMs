# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import next_palindrome as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\\\xc6\xca\x94\xd91\xc8@"
    module_0.next_palindrome(bytes_0)


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.next_palindrome(tuple_0)
    var_1 = module_0.next_palindrome(var_0)


def test_case_2():
    tuple_0 = ()
    var_0 = module_0.next_palindrome(tuple_0)
    var_1 = module_0.next_palindrome(var_0)
    var_2 = module_0.next_palindrome(var_0)
    var_3 = module_0.next_palindrome(var_0)
    var_4 = module_0.next_palindrome(var_2)
    var_5 = module_0.next_palindrome(var_0)
    var_6 = module_0.next_palindrome(var_1)
    var_7 = module_0.next_palindrome(var_1)
    var_8 = module_0.next_palindrome(var_3)
    var_9 = module_0.next_palindrome(var_3)


def test_case_3():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.next_palindrome(dict_0)