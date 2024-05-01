
import unittest
from temp_bug_qb import original_func as original_source
from temp_acc_qb import patched_func as patched_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['> <\r\r', '3']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['^ v', '3']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['< >\r\r', '2']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


if __name__ == '__main__':
    unittest.main()  
    
    