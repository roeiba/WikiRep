'''
Created on Sep 27, 2012

@author: roeib
'''
import unittest
import numpy

import test_utils 
from model import math_utils

class TestUtils(test_utils.TestBase):

    def test__centroid(self):
        vectors = numpy.array([ 
         [0,0,8], 
         [6,0,2], 
         [3,0,-5], 
        ])
        expected_vec = numpy.array([3,0,5.0/3])
        actual_vec = math_utils.get_vectors_centroid(vectors)
        self.assert_almost_equals(expected_vec, actual_vec, msg="Centroid wrong calculations!")
    

if __name__ == "__main__":
    unittest.main()