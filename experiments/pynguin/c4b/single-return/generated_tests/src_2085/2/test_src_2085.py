# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2085 as module_0


def test_case_0():
    str_0 = "(}#HY=!Az!G)bvd6fZd"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"


def test_case_1():
    str_0 = "(}#HY=!Az!G)bvd6fZd"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "f)7\x0cy1jQWj3i$l{|Ik"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    module_0.func()