# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2230 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x1fdqHT\xban-\xe4\xd7\xf2\xaf\xe7\x82-\xa3\xa3\xdbk"
    bytes_1 = b"\xc4J\xbfd)\x1f"
    list_0 = [bytes_0, bytes_1]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = '@mO-H^i7HQxv^"WW'
    str_1 = "5RLj"
    list_0 = [str_0, str_0, str_1]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    dict_0 = {str_0: str_0, str_1: str_0}
    module_1.object(*dict_0, **dict_0)