# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import to_base as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 3526.1
#    module_0.to_base(float_0, float_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -2797
    var_0 = module_0.to_base(int_0, int_0)
    assert var_0 == ""
    var_1 = module_0.to_base(int_0, int_0)
    assert var_1 == ""
    var_2 = module_0.to_base(int_0, int_0)
    assert var_2 == ""
#    var_1.safe_substitute(**var_1)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
#    module_0.to_base(none_type_0, none_type_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 560
    var_0 = module_0.to_base(int_0, int_0)
    assert var_0 == "10"
    none_type_0 = None
#    module_0.to_base(int_0, none_type_0)
