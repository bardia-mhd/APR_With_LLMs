# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_paths as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "kli\x0bI0Fg\r.VeHj!phNh"
    module_0.shortest_paths(str_0, str_0)


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.shortest_paths(tuple_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.shortest_paths(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"J\xea"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
    module_0.shortest_paths(bytes_0, dict_0)