# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xa8\x8d\xb5\x85\xa3\xc6{/\x13_BN\xef\xa8'\xdf\xb2\xef"
    var_0 = module_0.lis(bytes_0)
    assert var_0 == 6
    var_1 = module_0.lis(bytes_0)
    assert var_1 == 6
    var_2 = module_0.lis(bytes_0)
    assert var_2 == 6
    module_0.lis(var_2)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    module_0.lis(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xf3y8\xd7\xa4S\n\x87D\x82\xb43i\xf5"
    var_0 = module_0.lis(bytes_0)
    assert var_0 == 5
    bytes_1 = b"\xce!!\xef\x05)"
    var_1 = module_0.lis(bytes_1)
    assert var_1 == 2
    module_0.lis(var_1)