# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_514 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xa7\xe4\xa0\x1f\x19\x94\x81\xe2P&$w\x11\xdcO,_\xf6"
    int_0 = 568
    int_1 = 181
    tuple_0 = (bytes_0, int_0, int_1)
    set_0 = {tuple_0, bytes_0}
#    module_0.func(*set_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "A{CBkFwcbq$^Y&S"
    var_0 = module_0.func(*str_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
#    module_0.func(*list_0)