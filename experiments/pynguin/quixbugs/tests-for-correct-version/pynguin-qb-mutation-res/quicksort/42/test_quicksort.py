# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import quicksort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xf4\xdbK-\x8c)d\x1b$\xafz"
    set_0 = {bytes_0}
    module_0.quicksort(set_0)


def test_case_1():
    bool_0 = False
    var_0 = module_0.quicksort(bool_0)


def test_case_2():
    bytes_0 = b"\xde\xf2\xe9\xfd"
    var_0 = module_0.quicksort(bytes_0)
    var_1 = module_0.quicksort(var_0)