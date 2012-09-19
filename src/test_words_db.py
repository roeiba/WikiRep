'''
Created on Sep 19, 2012

@author: roeib
'''
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        v1 = [ 0.,  1.,  1.,  0.,  1.,  1.,  0.,  0.,  1.]
        v2 = [ 1.,  1.,  0.,  1.,  0.,  1.,  1.,  1.,  1.]
        
        all_words = {'noodl': 2, 'for': 1, 'read': 1, 'soul': 1, 'soup': 2, 'book': 1, 'chicken': 2, 'eat': 1, 'like': 1}
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()