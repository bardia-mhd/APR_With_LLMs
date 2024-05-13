
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "abcdefghijklmnopqrstuvwxyz@hostname.com"
        self.assertEqual(patched_source(input_0), original_source(input_0))
            


    def test1(self):
        input_1 = "abcdefghijklmnopqrstuvwxyz@hostname.com"
        self.assertEqual(patched_source(input_1), original_source(input_1))
            


    def test2(self):
        input_2 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(patched_source(input_2), original_source(input_2))
            


    def test3(self):
        input_3 = "test@this.is.a.long.hostname.that.is.over.32.characters.long"
        self.assertEqual(patched_source(input_3), original_source(input_3))
            


    def test4(self):
        input_4 = "abcdefghijklmnop@ABCDEFGHIJ123456.KLMNOPQR/STUVWXYZ"
        self.assertEqual(patched_source(input_4), original_source(input_4))
            


    def test5(self):
        input_5 = "a@b.c"
        self.assertEqual(patched_source(input_5), original_source(input_5))
            


    def test6(self):
        input_6 = "a@b.c"
        self.assertEqual(patched_source(input_6), original_source(input_6))
            


    def test7(self):
        input_7 = "abcdefghijk@abcde.abcde.abcde.abcde.abcde.abcde/123456"
        self.assertEqual(patched_source(input_7), original_source(input_7))
            


    def test8(self):
        input_8 = "a@b.c"
        self.assertEqual(patched_source(input_8), original_source(input_8))
            


if __name__ == '__main__':
    unittest.main()  
    
    