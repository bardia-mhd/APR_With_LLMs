# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_514 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"4"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "#=2BX1#ej"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".#.=.2.b.x.1.#.j"
#    module_0.func()