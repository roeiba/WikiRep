'''
Created on Sep 27, 2012

@author: roeib
'''
import unittest
from scipy.sparse import csr_matrix as matrix
import numpy
from test import test_utils 
from model import math_utils

class TestUtils(test_utils.TestBase):

    def test__centroid(self):
        vectors = [
            matrix([0,0,8]), 
            matrix([6,0,2]), 
            matrix([3,0,-5]), 
        ]
        expected_vec = matrix([3,0,5.0/3])
        actual_vec = math_utils.get_vectors_centroid(vectors)
        numpy.testing.assert_array_almost_equal(expected_vec.todense(), actual_vec.todense(), err_msg="Centroid wrong calculations!")
    

if __name__ == "__main__":
    unittest.main()