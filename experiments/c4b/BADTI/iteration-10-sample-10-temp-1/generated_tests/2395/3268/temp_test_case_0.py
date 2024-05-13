
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "6 2 8 4 3 1 9"
        self.assertEqual(patched_source(input_0), original_source(input_0))
            


    def test1(self):
        input_1 = "5 3 2 1 4 3"
        self.assertEqual(patched_source(input_1), original_source(input_1))
            


    def test2(self):
        input_2 = "2 7 1 8 2 8 9"
        self.assertEqual(patched_source(input_2), original_source(input_2))
            


    def test3(self):
        input_3 = "5 3 9 1 4 6"
        self.assertEqual(patched_source(input_3), original_source(input_3))
            


    def test4(self):
        input_4 = "3 5 7 9 2 8"
        self.assertEqual(patched_source(input_4), original_source(input_4))
            


    def test5(self):
        input_5 = "1 2 3 4 5 6"
        self.assertEqual(patched_source(input_5), original_source(input_5))
            


    def test6(self):
        input_6 = "3 2 7 5 1 4"
        self.assertEqual(patched_source(input_6), original_source(input_6))
            


    def test7(self):
        input_7 = "10 5 20 3 12 18"
        self.assertEqual(patched_source(input_7), original_source(input_7))
            


    def test8(self):
        input_8 = "3 6 1 9 7 5"
        self.assertEqual(patched_source(input_8), original_source(input_8))
            


    def test9(self):
        input_9 = "10 20 30 40 50 60"
        self.assertEqual(patched_source(input_9), original_source(input_9))
            


if __name__ == '__main__':
    unittest.main()  
    
    