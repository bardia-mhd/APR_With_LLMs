# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kth as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1690
    bytes_0 = b"Vk\x10\x18\x05\xa9p'\x17$6c\x98\xa9\x88\x00"
    module_0.kth(bytes_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    module_0.kth(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"Vk\x10\x18\x05\xa9p'\x17$6c\x98\xa9\x88\x00"
    bool_0 = False
    var_0 = module_0.kth(bytes_0, bool_0)
    assert var_0 == 0
    module_0.kth(bool_0, bool_0)