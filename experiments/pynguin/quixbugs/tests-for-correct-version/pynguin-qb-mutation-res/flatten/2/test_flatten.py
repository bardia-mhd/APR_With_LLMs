# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import flatten as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"\xdc\xf7\x9bK\xdf\xf8\x05\x18\xcf\xc5\xaf\x16\xc0\x01m\x06XS"
    var_0 = module_0.flatten(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"i\xa1<\x1dVq\xa5\x81"
    var_0 = module_0.flatten(bytes_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -1475
    var_0 = module_0.flatten(int_0)
    var_1 = module_0.flatten(int_0)
    complex_0 = -2388.4 - 3114.4j
    var_2 = module_0.flatten(var_0)
    var_3 = module_0.flatten(var_0)
    var_4 = module_0.flatten(complex_0)
    var_5 = module_0.flatten(var_4)
    list_0 = [int_0, var_4, complex_0, int_0]
    tuple_0 = (int_0, list_0)
    var_6 = module_0.flatten(var_0)
    var_7 = module_0.flatten(tuple_0)
    int_1 = -1367
    str_0 = "/\x0b&j%w+ "
    set_0 = {var_2, var_7, var_7, complex_0}
    var_8 = module_0.flatten(set_0)
    var_9 = module_0.flatten(var_2)
    var_10 = module_0.flatten(var_1)
    bool_0 = False
    var_11 = module_0.flatten(bool_0)
    var_12 = module_0.flatten(var_4)
    var_13 = module_0.flatten(var_0)
    tuple_1 = (int_1, str_0, str_0)
    var_14 = module_0.flatten(var_7)
    var_15 = module_0.flatten(complex_0)
    var_16 = module_0.flatten(var_13)
    var_17 = module_0.flatten(tuple_1)
    var_18 = module_0.flatten(str_0)
    var_19 = module_0.flatten(var_9)
    module_1.object(*var_14)