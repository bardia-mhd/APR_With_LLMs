# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_first_in_sorted as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xf7\x1f4"
    tuple_0 = (bytes_0, bytes_0)
    module_0.find_first_in_sorted(tuple_0, tuple_0)


def test_case_1():
    list_0 = []
    var_0 = module_0.find_first_in_sorted(list_0, list_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -402
    module_0.find_first_in_sorted(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = -2048.3
    list_0 = [float_0, float_0, float_0, float_0, float_0]
    var_0 = module_0.find_first_in_sorted(list_0, float_0)
    assert var_0 == 0
    module_0.find_first_in_sorted(float_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "3G,Z?_rc+SbJ"
    bool_0 = False
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1
    module_0.find_first_in_sorted(str_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    str_0 = "K\x0cv?#ikioE+$"
    tuple_0 = (set_0, str_0)
    var_0 = module_0.find_first_in_sorted(tuple_0, str_0)
    assert var_0 == 1
    float_0 = -2048.3
    list_0 = [float_0, float_0, float_0]
    var_1 = module_0.find_first_in_sorted(list_0, float_0)
    assert var_1 == 0
    module_1.object(*list_0)