# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1902 as module_0


def test_case_0():
    bool_0 = True
    set_0 = {bool_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == "I hate it"


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"L\xfe\xbc\xf5%%\xca\x95\xfa"
    var_0 = module_0.func(*bytes_0)
    assert (
        var_0
        == "I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love it"
    )
    bool_0 = True
    set_0 = {bool_0}
    var_1 = module_0.func(*set_0)
    assert var_1 == "I hate it"
    module_0.func()