# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_533 as module_0


def test_case_0():
    bytes_0 = b"\xad\xbcV\x8c<Q*\x05\xc6"
    var_0 = module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    complex_0 = -3087.0036 - 729.52j
    str_0 = "Es#h7r`0H}"
    int_0 = -5581
    set_0 = {str_0, int_0, str_0}
    tuple_0 = (complex_0, str_0, int_0, set_0)
    list_0 = [tuple_0, str_0, complex_0]
    var_0 = module_0.func(*list_0)