# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bucketsort as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b""
    int_0 = -460
    var_0 = module_0.bucketsort(bytes_0, int_0)
    float_0 = -1133.8
#    module_0.bucketsort(float_0, float_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xe2\x84n\xdeY\xba\xe0\x894\xa0W\x8c\xc0\xc6\x9e="
    bool_0 = False
    tuple_0 = (bytes_0, bool_0, bool_0, bool_0)
#    module_0.bucketsort(tuple_0, bool_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    complex_0 = -775.3548 + 1004.213j
#    module_0.bucketsort(complex_0, complex_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    set_0 = set()
    int_0 = -975
    var_0 = module_0.bucketsort(set_0, int_0)
    list_0 = [set_0, set_0]
    object_0 = module_1.object(*var_0)
    int_1 = 381
    var_1 = module_0.bucketsort(var_0, int_1)
#    module_0.bucketsort(set_0, list_0)
