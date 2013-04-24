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
        #arrane
        m = [[0.0,0.0],
             [1.0,1.0],
             [4.0,3.0]
             ]
        
        expected = [[0.0,0.0],
                    [1./2**0.5,1./2**0.5],
                    [0.8,0.6],
                    ]
        #act
        sm = sps.csr_matrix(m)
        mu.normalize(sm)
        actual = sm.todense()
        # assert
        np.testing.assert_allclose(actual,expected)


    def test__large_matrix_build(self):
        # here we get SparseEfficiencyWarning
        n = 10000
        T = sps.csr_matrix((n,n))
        for i in xrange(n):
            T[i,i]= 2*i

    def test__large_matrix_build2(self):
        print "-"*80
        n = 10000
        T = sps.dok_matrix((n,n))
        for i in xrange(n):
            T[i,i]= 2*i
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_normalization']
    unittest.main()