# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2647 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    bytes_0 = b"S\x15P^\t*=&\xef"
    list_0 = [bool_0, bytes_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xd0\xfeqH\xfd\x9b\xb3\xa0\x86\x16\x94!\t\x998%\xcag\x03\xaf"
    list_0 = module_0.func(*bytes_0)
    var_0 = module_0.func(*list_0)
    module_0.func()