# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import subsequences as module_0


def test_case_0():
    bool_0 = False
    var_0 = module_0.subsequences(bool_0, bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x00"
    module_0.subsequences(bytes_0, bytes_0, bytes_0)


def test_case_2():
    bool_0 = True
    bool_1 = False
    bool_2 = True
    var_0 = module_0.subsequences(bool_1, bool_2, bool_2)
    var_1 = module_0.subsequences(bool_0, var_0, bool_1)


def test_case_3():
    bool_0 = True
    var_0 = module_0.subsequences(bool_0, bool_0, bool_0)