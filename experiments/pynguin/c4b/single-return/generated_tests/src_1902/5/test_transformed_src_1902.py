# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1902 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"@\x94\x96d\xef\x06\x88\x12EwT\x82\xfc\xb98\xe4v\x1a"
    var_0 = module_0.func(*bytes_0)
    assert (
        var_0
        == "I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love it"
    )
#    module_0.func()


def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == " it"


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()