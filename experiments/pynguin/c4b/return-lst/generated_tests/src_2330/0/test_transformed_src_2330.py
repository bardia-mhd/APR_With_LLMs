# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2330 as module_0


def test_case_0():
    str_0 = "yU"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    bytes_0 = b"\xfc\xbb\x8f\x07\x17\xdb\x80}\x91\xf9\xe6\xc8\x0b\x01+\x18\xf2\x90"
    list_0 = [bytes_0, bytes_0]
    list_1 = [list_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_1)


def test_case_3():
    str_0 = "2v(dE[~aF"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, str_0]
    list_1 = [list_0, var_0, var_0]
    var_1 = module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = (
        b"\xa1\xbb\xda\x07\x17<\x80\xf2\x91\xf9\xe6\xc8\x0b\x01\xb5\xdc\x89\x18\xf2U"
    )
    list_0 = [bytes_0, bytes_0]
    list_1 = [list_0, bytes_0, bytes_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = 'jUEnH:K<Z|[GW4Y?"9>'
    var_0 = module_0.func(*str_0)
    bytes_0 = b"\xa1\xbb\x8f\x17\x80\xf0\xf2\x91\xf9\xe6\xc8\x0b\x01\x89\x18U"
    list_0 = [bytes_0, bytes_0]
    list_1 = [list_0, bytes_0, bytes_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "?U"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    list_1 = [var_0]
#    module_0.func(*list_1)