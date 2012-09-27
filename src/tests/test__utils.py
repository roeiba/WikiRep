'''
Created on Sep 27, 2012

@author: roeib
'''
import unittest
import numpy
import utilities as utils

    
class TestUtils(unittest.TestCase):

    def test__centroid(self):
        vectors = numpy.array([ 
         [0,0,8], 
         [6,0,2], 
         [3,0,-5], 
        ])
        expected_vec = numpy.array([3,0,5.0/3])
        actual_vec = utils.get_vectors_centroid(vectors)
        for i in range(3):
            self.assertAlmostEqual(expected_vec[i], actual_vec[i], 
                    msg="Centroid wrong calculations! expected {}, actual {}".format(expected_vec, actual_vec))


if __name__ == "__main__":
    unittest.main()