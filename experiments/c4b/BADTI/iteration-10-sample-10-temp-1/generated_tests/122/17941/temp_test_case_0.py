
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['250 250 250 250 250\r\r', '0 0 0 0 0\r\r', '1 1']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['20 40 60 80 100\r\r', '0 1 2 3 4\r\r', '1 10']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['0 0 0 0 0\r\r', '0 0 0 0 0\r\r', '0 0']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['250 250 250 250 250\r\r', '1 1 1 1 1\r\r', '1 1']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['30 50 70 90 110\r\r', '0 1 2 3 4\r\r', '1 0']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['100 200 300 400 500\r\r', '2 4 6 8 10\r\r', '3 2']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['30 50 70 90 110\r\r', '0 1 2 3 4\r\r', '1 0']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['10 20 30 40 50\r\r', '5 4 3 2 1\r\r', '2 3']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['250 250 250 250 250\r\r', '5 5 5 5 5\r\r', '1 0']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['50 100 150 200 250\r\r', '5 4 3 2 1\r\r', '2 1']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


if __name__ == '__main__':
    unittest.main()  
    
    