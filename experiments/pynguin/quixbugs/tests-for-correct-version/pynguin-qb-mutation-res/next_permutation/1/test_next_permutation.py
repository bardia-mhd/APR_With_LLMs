# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import next_permutation as module_0


def test_case_0():
    bytes_0 = b"\xa9\x047G\xba\x0c\xd9U\x83\xc4\xe8fl\x08\x99"
    var_0 = module_0.next_permutation(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x9agO\x17"
    var_0 = module_0.next_permutation(bytes_0)
    var_1 = module_0.next_permutation(bytes_0)
    module_0.next_permutation(var_1)


def test_case_2():
    bytes_0 = b"?<u\\3/\xd5\x98\xed`\xec("
    var_0 = module_0.next_permutation(bytes_0)