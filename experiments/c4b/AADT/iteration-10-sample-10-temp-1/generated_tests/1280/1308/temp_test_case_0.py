
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['2', '1 1']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['6', '2 3 5 7 11 13']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


if __name__ == '__main__':
    unittest.main()  
    
    