
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['8 3\r\r', '4 6']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['20 2\r\r', '9 19']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['21 3\r\r', '8 20']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['12 4\r\r', '18 9']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['80 10\r\r', '37 73']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['4 8\r\r', '14 7']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['27 3\r\r', '9 19']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['20 2\r\r', '9 19']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['15 3\r\r', '6 13']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['6 4\r\r', '9 21']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


    def test10(self):
        input_10 = ['20 2\r\r', '9 19\r']
        self.assertEqual(patched_source(*input_10), original_source(*input_10))
            


    def test11(self):
        input_11 = ['8 2\r\r', '2 3']
        self.assertEqual(patched_source(*input_11), original_source(*input_11))
            


    def test12(self):
        input_12 = ['10 5\r\r', '15 25']
        self.assertEqual(patched_source(*input_12), original_source(*input_12))
            


    def test13(self):
        input_13 = ['20 2\r\r', '2 19']
        self.assertEqual(patched_source(*input_13), original_source(*input_13))
            


    def test14(self):
        input_14 = ['100 30\r\r', '40 70']
        self.assertEqual(patched_source(*input_14), original_source(*input_14))
            


    def test15(self):
        input_15 = ['16 3\r\r', '5 13']
        self.assertEqual(patched_source(*input_15), original_source(*input_15))
            


    def test16(self):
        input_16 = ['20 2\r\r', '9 19']
        self.assertEqual(patched_source(*input_16), original_source(*input_16))
            


    def test17(self):
        input_17 = ['20 2\r\r', '9 19']
        self.assertEqual(patched_source(*input_17), original_source(*input_17))
            


    def test18(self):
        input_18 = ['10 5\r\r', '3 7']
        self.assertEqual(patched_source(*input_18), original_source(*input_18))
            


    def test19(self):
        input_19 = ['20 2\r\r', '9 20']
        self.assertEqual(patched_source(*input_19), original_source(*input_19))
            


    def test20(self):
        input_20 = ['50 5\r\r', '25 100']
        self.assertEqual(patched_source(*input_20), original_source(*input_20))
            


    def test21(self):
        input_21 = ['20 2\r\r', '9 19']
        self.assertEqual(patched_source(*input_21), original_source(*input_21))
            


    def test22(self):
        input_22 = ['20 2\r\r', '9 19']
        self.assertEqual(patched_source(*input_22), original_source(*input_22))
            


    def test23(self):
        input_23 = ['20 2\r\r', '9 19']
        self.assertEqual(patched_source(*input_23), original_source(*input_23))
            


    def test24(self):
        input_24 = ['8 5\r', '11 17']
        self.assertEqual(patched_source(*input_24), original_source(*input_24))
            


    def test25(self):
        input_25 = ['10 5\r\r', '15 10']
        self.assertEqual(patched_source(*input_25), original_source(*input_25))
            


    def test26(self):
        input_26 = ['22 3\r\r', '10 18']
        self.assertEqual(patched_source(*input_26), original_source(*input_26))
            


    def test27(self):
        input_27 = ['20 2\r\r', '9 20']
        self.assertEqual(patched_source(*input_27), original_source(*input_27))
            


    def test28(self):
        input_28 = ['1 2\r\r', '3 4']
        self.assertEqual(patched_source(*input_28), original_source(*input_28))
            


    def test29(self):
        input_29 = ['15 5\r\r', '25 35']
        self.assertEqual(patched_source(*input_29), original_source(*input_29))
            


    def test30(self):
        input_30 = ['20 2\r\r', '9 10']
        self.assertEqual(patched_source(*input_30), original_source(*input_30))
            


    def test31(self):
        input_31 = ['10 3\r\r', '6 11']
        self.assertEqual(patched_source(*input_31), original_source(*input_31))
            


    def test32(self):
        input_32 = ['20 2\r\r', '9 19']
        self.assertEqual(patched_source(*input_32), original_source(*input_32))
            


    def test33(self):
        input_33 = ['12 4\r\r', '22 19']
        self.assertEqual(patched_source(*input_33), original_source(*input_33))
            


    def test34(self):
        input_34 = ['20 2\r\r', '9 9']
        self.assertEqual(patched_source(*input_34), original_source(*input_34))
            


    def test35(self):
        input_35 = ['6 10\r', '15 14']
        self.assertEqual(patched_source(*input_35), original_source(*input_35))
            


    def test36(self):
        input_36 = ['20 2\r\r', '10 19']
        self.assertEqual(patched_source(*input_36), original_source(*input_36))
            


    def test37(self):
        input_37 = ['20 2\r\r', '9 19']
        self.assertEqual(patched_source(*input_37), original_source(*input_37))
            


    def test38(self):
        input_38 = ['18 2\r\r', '6 22']
        self.assertEqual(patched_source(*input_38), original_source(*input_38))
            


    def test39(self):
        input_39 = ['20 2\r\r', '9 19  ']
        self.assertEqual(patched_source(*input_39), original_source(*input_39))
            


    def test40(self):
        input_40 = ['20 3\r\r', '9 19']
        self.assertEqual(patched_source(*input_40), original_source(*input_40))
            


    def test41(self):
        input_41 = ['42 6\r\r', '15 27']
        self.assertEqual(patched_source(*input_41), original_source(*input_41))
            


    def test42(self):
        input_42 = ['30 4\r\r', '15 20']
        self.assertEqual(patched_source(*input_42), original_source(*input_42))
            


    def test43(self):
        input_43 = ['10 5\r\r', '8 20']
        self.assertEqual(patched_source(*input_43), original_source(*input_43))
            


    def test44(self):
        input_44 = ['11 5\r', '17 8']
        self.assertEqual(patched_source(*input_44), original_source(*input_44))
            


    def test45(self):
        input_45 = ['10 5\r', '5 5']
        self.assertEqual(patched_source(*input_45), original_source(*input_45))
            


    def test46(self):
        input_46 = ['20 2\r\r', '9 20']
        self.assertEqual(patched_source(*input_46), original_source(*input_46))
            


    def test47(self):
        input_47 = ['15 3\r\r', '5 10']
        self.assertEqual(patched_source(*input_47), original_source(*input_47))
            


    def test48(self):
        input_48 = ['10 2\r\r', '3 5']
        self.assertEqual(patched_source(*input_48), original_source(*input_48))
            


    def test49(self):
        input_49 = ['20 2\r\r', '9 18']
        self.assertEqual(patched_source(*input_49), original_source(*input_49))
            


    def test50(self):
        input_50 = ['24 2\r\r', '9 19']
        self.assertEqual(patched_source(*input_50), original_source(*input_50))
            


    def test51(self):
        input_51 = ['10 5\r\r', '9 3']
        self.assertEqual(patched_source(*input_51), original_source(*input_51))
            


    def test52(self):
        input_52 = ['5 3\r\r', '8 15']
        self.assertEqual(patched_source(*input_52), original_source(*input_52))
            


    def test53(self):
        input_53 = ['20 2\r\r', '10 19']
        self.assertEqual(patched_source(*input_53), original_source(*input_53))
            


    def test54(self):
        input_54 = ['3 5\r\r', '7 11']
        self.assertEqual(patched_source(*input_54), original_source(*input_54))
            


    def test55(self):
        input_55 = ['20 2\r\r', '9 19']
        self.assertEqual(patched_source(*input_55), original_source(*input_55))
            


    def test56(self):
        input_56 = ['1 2\r\r', '3 4']
        self.assertEqual(patched_source(*input_56), original_source(*input_56))
            


    def test57(self):
        input_57 = ['5 3\r', '9 19']
        self.assertEqual(patched_source(*input_57), original_source(*input_57))
            


    def test58(self):
        input_58 = ['10 5\r\r', '5 10']
        self.assertEqual(patched_source(*input_58), original_source(*input_58))
            


    def test59(self):
        input_59 = ['20 2\r\r', '10 19']
        self.assertEqual(patched_source(*input_59), original_source(*input_59))
            


    def test60(self):
        input_60 = "20 2 9 19"
        self.assertEqual(patched_source(input_60), original_source(input_60))
            


    def test61(self):
        input_61 = ['30 5\r\r', '18 25']
        self.assertEqual(patched_source(*input_61), original_source(*input_61))
            


    def test62(self):
        input_62 = ['15 3\r\r', '7 11']
        self.assertEqual(patched_source(*input_62), original_source(*input_62))
            


    def test63(self):
        input_63 = ['3 7', '5 11']
        self.assertEqual(patched_source(*input_63), original_source(*input_63))
            


    def test64(self):
        input_64 = ['10 5\r\r', '3 7']
        self.assertEqual(patched_source(*input_64), original_source(*input_64))
            


    def test65(self):
        input_65 = ['10 5\r', '6 12']
        self.assertEqual(patched_source(*input_65), original_source(*input_65))
            


    def test66(self):
        input_66 = ['7 6\r\r', '8 5']
        self.assertEqual(patched_source(*input_66), original_source(*input_66))
            


    def test67(self):
        input_67 = ['12 8\r\r', '5 16']
        self.assertEqual(patched_source(*input_67), original_source(*input_67))
            


    def test68(self):
        input_68 = ['20 2\r\r', '9 20']
        self.assertEqual(patched_source(*input_68), original_source(*input_68))
            


    def test69(self):
        input_69 = ['9 3\r\r', '8 10']
        self.assertEqual(patched_source(*input_69), original_source(*input_69))
            


    def test70(self):
        input_70 = ['20 2\r\r', '9 19']
        self.assertEqual(patched_source(*input_70), original_source(*input_70))
            


    def test71(self):
        input_71 = ['12 8\r\r', '6 20']
        self.assertEqual(patched_source(*input_71), original_source(*input_71))
            


    def test72(self):
        input_72 = ['20 20\r\r', '9 19']
        self.assertEqual(patched_source(*input_72), original_source(*input_72))
            


    def test73(self):
        input_73 = ['10 2\r\r', '3 15']
        self.assertEqual(patched_source(*input_73), original_source(*input_73))
            


    def test74(self):
        input_74 = ['8 6\r\r', '5 9']
        self.assertEqual(patched_source(*input_74), original_source(*input_74))
            


    def test75(self):
        input_75 = ['24 6\r\r', '9 21']
        self.assertEqual(patched_source(*input_75), original_source(*input_75))
            


    def test76(self):
        input_76 = ['20 2\r\r', '9 13']
        self.assertEqual(patched_source(*input_76), original_source(*input_76))
            


    def test77(self):
        input_77 = ['5 8\r\r', '7 21']
        self.assertEqual(patched_source(*input_77), original_source(*input_77))
            


    def test78(self):
        input_78 = ['24 8\r\r', '10 15']
        self.assertEqual(patched_source(*input_78), original_source(*input_78))
            


    def test79(self):
        input_79 = ['12 4\r\r', '9 19']
        self.assertEqual(patched_source(*input_79), original_source(*input_79))
            


    def test80(self):
        input_80 = ['14 2\r\r', '4 7']
        self.assertEqual(patched_source(*input_80), original_source(*input_80))
            


    def test81(self):
        input_81 = ['7 2\r\r', '5 13']
        self.assertEqual(patched_source(*input_81), original_source(*input_81))
            


    def test82(self):
        input_82 = ['20 2\r\r', '10 19']
        self.assertEqual(patched_source(*input_82), original_source(*input_82))
            


    def test83(self):
        input_83 = ['4 2\r', '3 5']
        self.assertEqual(patched_source(*input_83), original_source(*input_83))
            


    def test84(self):
        input_84 = ['35 7\r\r', '15 40']
        self.assertEqual(patched_source(*input_84), original_source(*input_84))
            


    def test85(self):
        input_85 = ['20 2\r\r', '9 19']
        self.assertEqual(patched_source(*input_85), original_source(*input_85))
            


    def test86(self):
        input_86 = ['20 5\r\r', '6 13']
        self.assertEqual(patched_source(*input_86), original_source(*input_86))
            


    def test87(self):
        input_87 = ['35 7\r\r', '8 19']
        self.assertEqual(patched_source(*input_87), original_source(*input_87))
            


    def test88(self):
        input_88 = ['27 3\r\r', '9 19']
        self.assertEqual(patched_source(*input_88), original_source(*input_88))
            


    def test89(self):
        input_89 = ['40 2\r\r', '3 75']
        self.assertEqual(patched_source(*input_89), original_source(*input_89))
            


    def test90(self):
        input_90 = ['30 3\r\r', '12 28']
        self.assertEqual(patched_source(*input_90), original_source(*input_90))
            


    def test91(self):
        input_91 = ['12 3\r\r', '8 24']
        self.assertEqual(patched_source(*input_91), original_source(*input_91))
            


    def test92(self):
        input_92 = ['10 5\r\r', '11 13']
        self.assertEqual(patched_source(*input_92), original_source(*input_92))
            


    def test93(self):
        input_93 = ['15 25\r\r', '8 14']
        self.assertEqual(patched_source(*input_93), original_source(*input_93))
            


    def test94(self):
        input_94 = ['10 5\r\r', '15 8']
        self.assertEqual(patched_source(*input_94), original_source(*input_94))
            


    def test95(self):
        input_95 = ['20 2\r\r', '9 19']
        self.assertEqual(patched_source(*input_95), original_source(*input_95))
            


    def test96(self):
        input_96 = ['10 3\r\r', '6 15']
        self.assertEqual(patched_source(*input_96), original_source(*input_96))
            


    def test97(self):
        input_97 = ['7 3\r', '12 8']
        self.assertEqual(patched_source(*input_97), original_source(*input_97))
            


    def test98(self):
        input_98 = ['20 2\r\r', '10 18']
        self.assertEqual(patched_source(*input_98), original_source(*input_98))
            


    def test99(self):
        input_99 = ['1 1\r\r', '1 1']
        self.assertEqual(patched_source(*input_99), original_source(*input_99))
            


if __name__ == '__main__':
    unittest.main()  
    
    