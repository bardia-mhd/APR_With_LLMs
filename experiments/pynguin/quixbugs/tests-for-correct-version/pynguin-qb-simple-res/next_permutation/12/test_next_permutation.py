# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import next_permutation as module_0


def test_case_0():
    str_0 = ".p8zLbi7Tp`<m:_9E6\r"
    var_0 = module_0.next_permutation(str_0)


def test_case_1():
    bytes_0 = b""
    var_0 = module_0.next_permutation(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.next_permutation(bool_0)