
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['7\r', '14']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['2\r', '16']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['2\r', '8']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['7\r', '98']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['7\r', '49']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['5\r', '30']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['6\r', '216']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['2\r', '8']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['6\r', '216']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['7\r', '98']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


if __name__ == '__main__':
    unittest.main()  
    
    