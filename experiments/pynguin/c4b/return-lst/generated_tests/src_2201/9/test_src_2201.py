# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2201 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"-\xd8\x86\x16\xc1\xffh\xbb\x90'\xe3\xe4Hz:"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"-\xd8\x86\x16\xc1\xdb\xffh\xbb\x90'\xe3\xb5\xe4Hz:n"
    var_0 = module_0.func(*bytes_0)
    list_0 = module_0.func(*var_0)
    var_1 = module_0.func(*list_0)
    var_2 = module_0.func(*list_0)
    module_0.func()