# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import flatten as module_0
import builtins as module_1


def test_case_0():
    bool_0 = False
    var_0 = module_0.flatten(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x86\x14\xe7=\x86n0{'\x06G\xd9\xe6z\x90{\x03"
    var_0 = module_0.flatten(bytes_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"5K\xeb\xdf\x04"
    var_0 = module_0.flatten(bytes_0)
    var_1 = module_0.flatten(var_0)
    var_2 = module_0.flatten(bytes_0)
    var_3 = module_0.flatten(var_0)
    var_4 = module_0.flatten(var_0)
    var_5 = module_0.flatten(var_2)
    var_6 = module_0.flatten(var_3)
    list_0 = [var_5]
    list_1 = [var_3, var_5, var_1, list_0]
    var_7 = module_0.flatten(list_1)
    module_1.object(*var_7)