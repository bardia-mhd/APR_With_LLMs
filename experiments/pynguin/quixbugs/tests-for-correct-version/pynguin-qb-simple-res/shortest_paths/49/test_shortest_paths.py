# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_paths as module_0


def test_case_0():
    str_0 = ""
    var_0 = module_0.shortest_paths(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"v\xfb\xdc\xa4\x96\xba\xfcX\x82+\xbdA7X\xbd\xd2h"
    bool_0 = True
    module_0.shortest_paths(bool_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -786.0
    tuple_0 = (float_0, float_0)
    dict_0 = {}
    var_0 = module_0.shortest_paths(float_0, dict_0)
    tuple_1 = (tuple_0,)
    module_0.shortest_paths(tuple_1, tuple_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = -786.0
    tuple_0 = (float_0, float_0)
    dict_0 = {tuple_0: tuple_0, tuple_0: float_0}
    var_0 = module_0.shortest_paths(tuple_0, dict_0)
    module_0.shortest_paths(float_0, float_0)