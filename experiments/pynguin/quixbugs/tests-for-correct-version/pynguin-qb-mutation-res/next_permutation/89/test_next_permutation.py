# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import next_permutation as module_0


def test_case_0():
    bytes_0 = b"\xc2\xea\xdaW-\x13?[\xff\xf4bj\xbd\x01\x80=\xa6"
    var_0 = module_0.next_permutation(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b""
    var_0 = module_0.next_permutation(bytes_0)
    module_0.next_permutation(var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.next_permutation(bool_0)


def test_case_3():
    bytes_0 = b"\xaf\xcc=-1\xfau\xa9x\x0b\xca\xa3\xd2\xbb\xc03\x7f\xf7;"
    var_0 = module_0.next_permutation(bytes_0)