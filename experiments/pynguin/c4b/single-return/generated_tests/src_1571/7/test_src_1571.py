# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1571 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = ",\n&U"
    float_0 = -940.3907583996869
    list_0 = [str_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ",\n&u"
    var_1 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = ",\nBU"
    var_0 = module_0.func(*str_0)
    assert var_0 == ","
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "N'h\"E5g.aW#-3T"
    float_0 = -964.6852
    list_0 = [str_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "N'h\"E5g.aW#-3T"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "i&U$"
    float_0 = -972.6858758947333
    list_0 = [str_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "I&u$"
    module_1.object(*float_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = ""
    float_0 = -970.565662893726
    list_0 = [str_0, float_0]
    var_0 = module_0.func(*list_0)
    module_1.object(*var_0)