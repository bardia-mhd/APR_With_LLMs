
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['WBWBWBWB\r', 'BBBBBBBB\r', 'WBWBWBWB\r', 'WBWBWBWB\r', 'WBWBWBWB\r', 'WBWBWBWB\r', 'WBWBWBWB\r', 'WBWBWBWB']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['WWBWBBBW\r', 'BBBBBBBB\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['BWBWBWBW\r', 'BBBBBBBB\r', 'BWBWBWBW\r', 'BWBWBWBW\r', 'BWBWBWBW\r', 'BWBWBWBW\r', 'BWBWBWBW\r', 'BWBWBWBW']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['WWWBWWBW\r', 'BBBBBBBB\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['BBBWBBBW\r', 'BBBWBBBW\r', 'BBBWBBBW\r', 'BBBWBBBW\r', 'BBBWBBBW\r', 'BBBWBBBW\r', 'BBBWBBBW\r', 'BBBWBBBW']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


if __name__ == '__main__':
    unittest.main()  
    
    