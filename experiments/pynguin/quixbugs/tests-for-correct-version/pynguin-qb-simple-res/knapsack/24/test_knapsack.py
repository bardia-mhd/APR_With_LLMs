# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b".\x81\xca\xe4\xc7\x1c<\xafHcQB\xb7\x82\x8b1\x88\xba\xb4L"
    module_0.knapsack(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"/<\x0f\x84\xac"
    tuple_0 = ()
    var_0 = module_0.knapsack(bytes_0, tuple_0)
    assert var_0 == 0
    module_0.knapsack(tuple_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.knapsack(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    tuple_0 = (list_0, bool_0, list_0, list_0)
    module_0.knapsack(bool_0, tuple_0)