# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import to_base as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 1137.75967
    none_type_0 = None
    module_0.to_base(float_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -219.0
    var_0 = module_0.to_base(float_0, float_0)
    assert var_0 == ""
    bytes_0 = b"\x11\xa7\xcb\n\xe2\xbe\xc2\xd08\xe6\xbc!\x1ab\x9b"
    var_1 = module_0.to_base(float_0, float_0)
    assert var_1 == ""
    module_0.to_base(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.to_base(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 1592
    var_0 = module_0.to_base(int_0, int_0)
    assert var_0 == "10"
    var_1 = module_0.to_base(int_0, int_0)
    assert var_1 == "10"
    var_1.__contains__(int_0)