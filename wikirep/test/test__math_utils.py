'''
Created on Apr 24, 2013

@author: inesmeya
'''
import unittest
import scipy as sp
import scipy.sparse as sps
import model.math_utils as mu
import numpy as np

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_l2_normalization(self):
        m = [[0.0,0.0],
             [1.0,1.0],
             [4.0,3.0]
             ]
        
        expected = [[0.0,0.0],
                    [1./2**0.5,1./2**0.5],
                    [0.8,0.6],
                    ]
        
        sm = sps.csr_matrix(m)
        mu.normalize(sm)
        actual = sm.todense()
        np.testing.assert_allclose(actual,expected)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_normalization']
    unittest.main()