# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import next_permutation as module_0


def test_case_0():
    str_0 = "5kbtt}o\t Q5I*<U2UW_"
    var_0 = module_0.next_permutation(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    var_0 = module_0.next_permutation(dict_0)
    var_1 = module_0.next_permutation(dict_0)
    var_2 = module_0.next_permutation(dict_0)
    module_0.next_permutation(var_1)


def test_case_2():
    bytes_0 = b"\xef9Y\xcf\xd5r \x0bQ\x8c\xff\xea"
    var_0 = module_0.next_permutation(bytes_0)


def test_case_3():
    str_0 = "rOV.ukq\nXPu]]j2"
    var_0 = module_0.next_permutation(str_0)