# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_897 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "uvm-AUA7~mJLXlu"
    var_0 = module_0.func(*str_0)
#    module_0.func()


def test_case_1():
    pass


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "<;H00<P"
    list_0 = []
    bytes_0 = b"\xd5\x08HjO\x8d\xa2\x0c]5\xae\r\xb2\xbeu"
    int_0 = 4027
    tuple_0 = (str_0, list_0, bytes_0, int_0)
    var_0 = module_0.func(*tuple_0)
    bytes_1 = b"s\xadA\xdb"
#    module_0.func(*bytes_1)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"(\x93\xbf\x85\x0f\xdad\xa3\x91\xd4\xd8"
    complex_0 = -217 + 1639.344j
    list_0 = [bytes_0, complex_0, complex_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x06a/\xdd\x857SN"
    dict_0 = {}
    list_0 = [dict_0, dict_0]
    list_1 = [dict_0, bytes_0, list_0]
    var_0 = module_0.func(*list_1)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\x06a/\xdd\x85\xcc7SN"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    list_0 = [dict_0, dict_0, dict_0, dict_0, dict_0, dict_0, dict_0, dict_0]
    list_1 = [list_0]
    var_0 = module_0.func(*list_1)
    var_1 = module_0.func(*var_0)
#    module_0.func()