# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_paths as module_0


def test_case_0():
    dict_0 = {}
    bool_0 = False
    var_0 = module_0.shortest_paths(bool_0, dict_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xdb\x18I\xc7\x1ap"
#    module_0.shortest_paths(bytes_0, bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
#    module_0.shortest_paths(none_type_0, none_type_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    tuple_0 = ()
    complex_0 = 356.37534582329715 + 122.3j
    tuple_1 = (tuple_0, complex_0)
    var_0 = module_0.shortest_paths(tuple_1, tuple_0)
    none_type_0 = None
#    module_0.shortest_paths(none_type_0, var_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    tuple_0 = ()
    complex_0 = 356.37534582329715 + 122.3j
    tuple_1 = (tuple_0, complex_0)
    var_0 = module_0.shortest_paths(tuple_1, tuple_0)
    var_1 = module_0.shortest_paths(tuple_0, var_0)
    none_type_0 = None
#    module_0.shortest_paths(none_type_0, var_0)