# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0
import builtins as module_1


def test_case_0():
    str_0 = "*kbH-L>)3;+z[Szd"
    var_0 = module_0.lis(str_0)
    assert var_0 == 6


def test_case_1():
    set_0 = set()
    var_0 = module_0.lis(set_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"Ss\x86\x9d\x7f\x9a\xcaX\x7f\xc26"
    tuple_0 = (bytes_0,)
    var_0 = module_0.lis(bytes_0)
    assert var_0 == 5
    set_0 = {tuple_0}
    tuple_1 = (set_0,)
#    module_1.object(*tuple_1)