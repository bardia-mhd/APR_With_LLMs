# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kth as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "k8u\rSabc"
    module_0.kth(str_0, str_0)


def test_case_1():
    int_0 = 153
    list_0 = [int_0, int_0]
    bytes_0 = b">\xc0\xc9d\xfb\xc2\xda\x86\xe3|d\xe1\xd9X\xe2\xb8"
    bool_0 = True
    var_0 = module_0.kth(bytes_0, bool_0)
    assert var_0 == 88
    var_1 = module_0.kth(list_0, bool_0)
    assert var_1 == 153


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 1251
    list_0 = [int_0]
    module_0.kth(list_0, int_0)