# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kheapsort as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"NZ\x12\x98\xa4C\x88g\xf4x\x1aj\x02$jD7\x9d\x04"
    var_0 = module_0.kheapsort(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"b'\xe6\xaa\xf6\x1e "
    list_0 = [bytes_0, bytes_0, bytes_0]
    none_type_0 = None
    var_0 = module_0.kheapsort(list_0, none_type_0)
    module_1.object(*var_0)


def test_case_2():
    list_0 = []
    none_type_0 = None
    var_0 = module_0.kheapsort(list_0, none_type_0)
    object_0 = module_1.object(*var_0)
    var_1 = module_0.kheapsort(none_type_0, object_0)
    var_2 = module_0.kheapsort(object_0, var_0)