'''
Created on Sep 27, 2012

@author: roeib
'''
import unittest
    
class TestBase(unittest.TestCase):
    def assert_almost_equals(self, expected, actual, msg=None):
        self.assertEqual(len(expected), len(actual), "dimensions mismatch")
        for i in xrange(len(expected)):
            self.assertAlmostEqual(expected[i], actual[i], msg="expected {}, actual {}".format(expected, actual) + str(msg))
        