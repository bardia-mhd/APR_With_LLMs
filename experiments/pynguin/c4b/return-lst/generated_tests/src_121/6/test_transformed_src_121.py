# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_121 as module_0


def test_case_0():
    int_0 = 2397
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    str_0 = "r\x0c]pg9v&BSp6!\x0bY\\"
    bool_1 = True
    float_0 = -1986.7
    tuple_0 = (str_0, bool_1, float_0)
    list_0 = [bool_0, bool_0, tuple_0, str_0]
    var_0 = module_0.func(*list_0)
    list_1 = [var_0, str_0, tuple_0]
#    module_0.func(*list_1)