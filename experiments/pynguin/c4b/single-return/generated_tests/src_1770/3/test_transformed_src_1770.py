# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1770 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 2199
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert (
        var_0
        == 91122661391549274157005307427909034807107843384063795627561681241947867206034964434524384852628006970864875205573040161301879845239624156037617779176731423352824478450087561261399758854367966544269360032841317494235584083934777466446379745813793908543664308274304009971283115602963482984596619741599720480481035342857110489459965957973874857091920607770255465145977695626211624721219053462866438442803461931774045868771401110123816782647988836479083703521189602472843266090037434075670985814705088402858603257692403221230656433562120523122315447108538348365381866533752212886796554757374730396050635378101837277686767806513551312023887553658238818317987676684288
    )
    int_1 = -1398
    int_2 = -1514
    list_1 = [int_1, int_2]
    var_1 = module_0.func(*list_1)
    assert var_1 == pytest.approx(0.0, abs=0.01, rel=0.01)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()