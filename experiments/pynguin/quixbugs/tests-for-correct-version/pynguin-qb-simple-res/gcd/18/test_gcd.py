# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import gcd as module_0


def test_case_0():
    bytes_0 = b"\xd3\x13}r\x80\x05u\xb8\xf76E7\xf4\xc0"
    bool_0 = False
    var_0 = module_0.gcd(bytes_0, bool_0)
    assert var_0 == b"\xd3\x13}r\x80\x05u\xb8\xf76E7\xf4\xc0"
    set_0 = {bool_0}
    var_1 = module_0.gcd(set_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    set_0 = {none_type_0}
    module_0.gcd(none_type_0, set_0)