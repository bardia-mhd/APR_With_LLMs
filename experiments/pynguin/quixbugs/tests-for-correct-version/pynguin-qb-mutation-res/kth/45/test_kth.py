# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kth as module_0


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.kth(list_0, bool_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    bool_1 = True
    module_0.kth(dict_0, bool_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = " BVg\x0c*>)le"
    bool_0 = False
    var_0 = module_0.kth(str_0, bool_0)
    assert var_0 == "\x0c"
    bytes_0 = b"\x12\x80\x87\xe0x5]\x93\x90\xa8B\xbe"
    module_0.kth(bytes_0, bytes_0)