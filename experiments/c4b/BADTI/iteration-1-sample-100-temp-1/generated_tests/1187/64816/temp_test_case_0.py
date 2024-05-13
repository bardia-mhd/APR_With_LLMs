
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "TesTing Case"
        self.assertEqual(patched_source(input_0), original_source(input_0))
            


    def test1(self):
        input_1 = "tEST eXAMPLE"
        self.assertEqual(patched_source(input_1), original_source(input_1))
            


    def test2(self):
        input_2 = "hello WORLD"
        self.assertEqual(patched_source(input_2), original_source(input_2))
            


    def test3(self):
        input_3 = "Caps"
        self.assertEqual(patched_source(input_3), original_source(input_3))
            


    def test4(self):
        input_4 = "aPPLE PiE"
        self.assertEqual(patched_source(input_4), original_source(input_4))
            


    def test5(self):
        input_5 = "cApS"
        self.assertEqual(patched_source(input_5), original_source(input_5))
            


    def test6(self):
        input_6 = "aBCDE fgh IJKL"
        self.assertEqual(patched_source(input_6), original_source(input_6))
            


    def test7(self):
        input_7 = "CapS"
        self.assertEqual(patched_source(input_7), original_source(input_7))
            


    def test8(self):
        input_8 = "cAPS aCCIDENT aCCIDENT"
        self.assertEqual(patched_source(input_8), original_source(input_8))
            


    def test9(self):
        input_9 = "AbCdEfGh IjKlMnOp"
        self.assertEqual(patched_source(input_9), original_source(input_9))
            


    def test10(self):
        input_10 = "Taco tuesday"
        self.assertEqual(patched_source(input_10), original_source(input_10))
            


    def test11(self):
        input_11 = "TeSt"
        self.assertEqual(patched_source(input_11), original_source(input_11))
            


    def test12(self):
        input_12 = "HelLo"
        self.assertEqual(patched_source(input_12), original_source(input_12))
            


    def test13(self):
        input_13 = "aBCD EFg"
        self.assertEqual(patched_source(input_13), original_source(input_13))
            


    def test14(self):
        input_14 = "Taco Truck"
        self.assertEqual(patched_source(input_14), original_source(input_14))
            


    def test15(self):
        input_15 = "JUnit testing"
        self.assertEqual(patched_source(input_15), original_source(input_15))
            


    def test16(self):
        input_16 = "ABcde"
        self.assertEqual(patched_source(input_16), original_source(input_16))
            


    def test17(self):
        input_17 = "tEst"
        self.assertEqual(patched_source(input_17), original_source(input_17))
            


    def test18(self):
        input_18 = "aBc Def"
        self.assertEqual(patched_source(input_18), original_source(input_18))
            


    def test19(self):
        input_19 = "TesT FOr sOmE caPSLOCK wORDS"
        self.assertEqual(patched_source(input_19), original_source(input_19))
            


    def test20(self):
        input_20 = "RaNdOm TeXT"
        self.assertEqual(patched_source(input_20), original_source(input_20))
            


    def test21(self):
        input_21 = "cAPs"
        self.assertEqual(patched_source(input_21), original_source(input_21))
            


    def test22(self):
        input_22 = "baNAna"
        self.assertEqual(patched_source(input_22), original_source(input_22))
            


    def test23(self):
        input_23 = "aBCD eFGH iJKL"
        self.assertEqual(patched_source(input_23), original_source(input_23))
            


    def test24(self):
        input_24 = "AbCDe fGHiJ"
        self.assertEqual(patched_source(input_24), original_source(input_24))
            


    def test25(self):
        input_25 = "cAPs"
        self.assertEqual(patched_source(input_25), original_source(input_25))
            


    def test26(self):
        input_26 = "sWApcaSe CaPsLoCk"
        self.assertEqual(patched_source(input_26), original_source(input_26))
            


    def test27(self):
        input_27 = "A accidentally"
        self.assertEqual(patched_source(input_27), original_source(input_27))
            


    def test28(self):
        input_28 = "tHIS iS a teSt"
        self.assertEqual(patched_source(input_28), original_source(input_28))
            


    def test29(self):
        input_29 = "HELLO world"
        self.assertEqual(patched_source(input_29), original_source(input_29))
            


    def test30(self):
        input_30 = "CAPsLoCK"
        self.assertEqual(patched_source(input_30), original_source(input_30))
            


    def test31(self):
        input_31 = "cApS cApS"
        self.assertEqual(patched_source(input_31), original_source(input_31))
            


    def test32(self):
        input_32 = "hElLo WoRlD"
        self.assertEqual(patched_source(input_32), original_source(input_32))
            


    def test33(self):
        input_33 = "accident"
        self.assertEqual(patched_source(input_33), original_source(input_33))
            


    def test34(self):
        input_34 = "tEsT Case"
        self.assertEqual(patched_source(input_34), original_source(input_34))
            


    def test35(self):
        input_35 = "Caps CaPs"
        self.assertEqual(patched_source(input_35), original_source(input_35))
            


    def test36(self):
        input_36 = "Aaa bbb"
        self.assertEqual(patched_source(input_36), original_source(input_36))
            


    def test37(self):
        input_37 = "HELLO World"
        self.assertEqual(patched_source(input_37), original_source(input_37))
            


    def test38(self):
        input_38 = "TastY TeSt"
        self.assertEqual(patched_source(input_38), original_source(input_38))
            


    def test39(self):
        input_39 = "aBCD efgh"
        self.assertEqual(patched_source(input_39), original_source(input_39))
            


    def test40(self):
        input_40 = "cAPs Lock"
        self.assertEqual(patched_source(input_40), original_source(input_40))
            


    def test41(self):
        input_41 = "PytHon"
        self.assertEqual(patched_source(input_41), original_source(input_41))
            


    def test42(self):
        input_42 = "CaPs loCk mE"
        self.assertEqual(patched_source(input_42), original_source(input_42))
            


    def test43(self):
        input_43 = "aBCD eFGH"
        self.assertEqual(patched_source(input_43), original_source(input_43))
            


    def test44(self):
        input_44 = "tHIS Is A Test"
        self.assertEqual(patched_source(input_44), original_source(input_44))
            


    def test45(self):
        input_45 = "cAPS one"
        self.assertEqual(patched_source(input_45), original_source(input_45))
            


    def test46(self):
        input_46 = "CAPS lock"
        self.assertEqual(patched_source(input_46), original_source(input_46))
            


    def test47(self):
        input_47 = "My caT is Black"
        self.assertEqual(patched_source(input_47), original_source(input_47))
            


    def test48(self):
        input_48 = "caPS loCK"
        self.assertEqual(patched_source(input_48), original_source(input_48))
            


    def test49(self):
        input_49 = "aPPLE bANANA oRANGE"
        self.assertEqual(patched_source(input_49), original_source(input_49))
            


    def test50(self):
        input_50 = "This is A Test string"
        self.assertEqual(patched_source(input_50), original_source(input_50))
            


    def test51(self):
        input_51 = "Hello WorlD"
        self.assertEqual(patched_source(input_51), original_source(input_51))
            


    def test52(self):
        input_52 = "Title Case"
        self.assertEqual(patched_source(input_52), original_source(input_52))
            


    def test53(self):
        input_53 = "PyThOn"
        self.assertEqual(patched_source(input_53), original_source(input_53))
            


    def test54(self):
        input_54 = "accIDent hAPPer"
        self.assertEqual(patched_source(input_54), original_source(input_54))
            


    def test55(self):
        input_55 = "aBC DEF Ghi"
        self.assertEqual(patched_source(input_55), original_source(input_55))
            


    def test56(self):
        input_56 = "Caps Lock"
        self.assertEqual(patched_source(input_56), original_source(input_56))
            


    def test57(self):
        input_57 = "CapS sWiTch"
        self.assertEqual(patched_source(input_57), original_source(input_57))
            


    def test58(self):
        input_58 = "TeStIng ProGram"
        self.assertEqual(patched_source(input_58), original_source(input_58))
            


    def test59(self):
        input_59 = "aAAaaa Aa"
        self.assertEqual(patched_source(input_59), original_source(input_59))
            


    def test60(self):
        input_60 = "aBCdEf ghiJKL"
        self.assertEqual(patched_source(input_60), original_source(input_60))
            


    def test61(self):
        input_61 = "Accidentally"
        self.assertEqual(patched_source(input_61), original_source(input_61))
            


    def test62(self):
        input_62 = "CaPS wOrLD"
        self.assertEqual(patched_source(input_62), original_source(input_62))
            


    def test63(self):
        input_63 = "CaPs"
        self.assertEqual(patched_source(input_63), original_source(input_63))
            


    def test64(self):
        input_64 = "HELLO World"
        self.assertEqual(patched_source(input_64), original_source(input_64))
            


    def test65(self):
        input_65 = "tHIS iS a TesT iNPUT"
        self.assertEqual(patched_source(input_65), original_source(input_65))
            


    def test66(self):
        input_66 = "HELLO world"
        self.assertEqual(patched_source(input_66), original_source(input_66))
            


    def test67(self):
        input_67 = "cAPs"
        self.assertEqual(patched_source(input_67), original_source(input_67))
            


    def test68(self):
        input_68 = "Hello WORld"
        self.assertEqual(patched_source(input_68), original_source(input_68))
            


    def test69(self):
        input_69 = "HELLO world"
        self.assertEqual(patched_source(input_69), original_source(input_69))
            


    def test70(self):
        input_70 = "Caps LoCKed"
        self.assertEqual(patched_source(input_70), original_source(input_70))
            


    def test71(self):
        input_71 = "aPPPle"
        self.assertEqual(patched_source(input_71), original_source(input_71))
            


    def test72(self):
        input_72 = "eXample TesT"
        self.assertEqual(patched_source(input_72), original_source(input_72))
            


    def test73(self):
        input_73 = "cAPS up"
        self.assertEqual(patched_source(input_73), original_source(input_73))
            


    def test74(self):
        input_74 = "CaPs LoCk"
        self.assertEqual(patched_source(input_74), original_source(input_74))
            


    def test75(self):
        input_75 = "aBCdEf"
        self.assertEqual(patched_source(input_75), original_source(input_75))
            


    def test76(self):
        input_76 = "hELLo WoRLd"
        self.assertEqual(patched_source(input_76), original_source(input_76))
            


    def test77(self):
        input_77 = "tEst sTring"
        self.assertEqual(patched_source(input_77), original_source(input_77))
            


    def test78(self):
        input_78 = "flY aCaDeMy"
        self.assertEqual(patched_source(input_78), original_source(input_78))
            


    def test79(self):
        input_79 = "cAPTain America"
        self.assertEqual(patched_source(input_79), original_source(input_79))
            


    def test80(self):
        input_80 = "aBCD eFGh"
        self.assertEqual(patched_source(input_80), original_source(input_80))
            


    def test81(self):
        input_81 = "AbC"
        self.assertEqual(patched_source(input_81), original_source(input_81))
            


    def test82(self):
        input_82 = "sEVERAL Tests"
        self.assertEqual(patched_source(input_82), original_source(input_82))
            


    def test83(self):
        input_83 = "CaPs"
        self.assertEqual(patched_source(input_83), original_source(input_83))
            


    def test84(self):
        input_84 = "PyThOn"
        self.assertEqual(patched_source(input_84), original_source(input_84))
            


    def test85(self):
        input_85 = "A sample Input"
        self.assertEqual(patched_source(input_85), original_source(input_85))
            


    def test86(self):
        input_86 = "aBC DEF"
        self.assertEqual(patched_source(input_86), original_source(input_86))
            


    def test87(self):
        input_87 = "tEst tEST"
        self.assertEqual(patched_source(input_87), original_source(input_87))
            


    def test88(self):
        input_88 = "aBCD eFGH"
        self.assertEqual(patched_source(input_88), original_source(input_88))
            


    def test89(self):
        input_89 = "Abcdef"
        self.assertEqual(patched_source(input_89), original_source(input_89))
            


    def test90(self):
        input_90 = "AaAa"
        self.assertEqual(patched_source(input_90), original_source(input_90))
            


    def test91(self):
        input_91 = "Upper casE"
        self.assertEqual(patched_source(input_91), original_source(input_91))
            


    def test92(self):
        input_92 = "cApS caPS"
        self.assertEqual(patched_source(input_92), original_source(input_92))
            


    def test93(self):
        input_93 = "Python Testing"
        self.assertEqual(patched_source(input_93), original_source(input_93))
            


    def test94(self):
        input_94 = "Title case"
        self.assertEqual(patched_source(input_94), original_source(input_94))
            


    def test95(self):
        input_95 = "Aabb Ccdd"
        self.assertEqual(patched_source(input_95), original_source(input_95))
            


    def test96(self):
        input_96 = "Accidental case"
        self.assertEqual(patched_source(input_96), original_source(input_96))
            


    def test97(self):
        input_97 = "cAPS lOCKED"
        self.assertEqual(patched_source(input_97), original_source(input_97))
            


if __name__ == '__main__':
    unittest.main()  
    
    