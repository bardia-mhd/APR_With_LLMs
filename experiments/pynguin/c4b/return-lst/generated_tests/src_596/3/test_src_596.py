# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_596 as module_0
import builtins as module_1


def test_case_0():
    int_0 = -1585
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"Pi\x0c\xe5Wi\xfby1\xd8\xa8\xeb\xf7g\x03\x86"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\t\x82vc\x07\x1a\x02u\xd28\xc3\xcc\xf3"
    var_0 = module_0.func(*bytes_0)
    object_0 = module_1.object()
    module_0.func()