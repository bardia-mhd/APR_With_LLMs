# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import max_sublist_sum as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -1799.4
    bytes_0 = b":<@\xe3A?V_9\xb5\x1b\x0b\xa6LFG"
    dict_0 = {float_0: float_0, float_0: bytes_0, bytes_0: bytes_0}
    module_0.max_sublist_sum(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xf8yZ\x05\xf1?M\xa1\xc4\xaf\xf6\xe1d\xe8\t\xec\xe1\xa7\xaf\xe9"
    var_0 = module_0.max_sublist_sum(bytes_0)
    assert var_0 == 3225
    bytes_1 = b"[\x9c\x88"
    var_1 = module_0.max_sublist_sum(bytes_1)
    assert var_1 == 383
    module_0.max_sublist_sum(var_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.max_sublist_sum(bool_0)