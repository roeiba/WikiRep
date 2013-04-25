'''
Created on Sep 19, 2012
'''
from model.semantic_interpreter import SemanticComparer
from model.database_wrapper import DatabaseWrapper
import unittest
import numpy
from test.test_utils import TestBase
from scipy.sparse import csr_matrix as matrix

#model
from model.stemmers import StopWordsStemmer

class TestSemanticIntepreter(TestBase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def getSimpleDb(self):
        concepts_index=['c1','c2']
        words_index=['a','b','c']
        wieght_matrix =matrix(
              [[0.5, 0.5],
               [0.2, 0.8],
               [1.0, 0.0]])
        db = DatabaseWrapper( wieght_matrix, concepts_index, words_index, StopWordsStemmer([]))
        return db

# ------------------------   Tests -----------------------------------

    def test_init(self):
        # arrange
        db = self.getSimpleDb()
        

    def test_simple(self):
        # arrange
        db = self.getSimpleDb()
        
        text = "a b c"
           
        expected = matrix([1.7/3, 1.3/3])
        # act
        actual  = db.get_text_centroid(text)
        numpy.testing.assert_array_almost_equal(expected.todense(), actual.todense(), err_msg="wrong centroid")
        
    def test_words_not_in_corpus(self):
        # arrange
        db = self.getSimpleDb()
        
        text = "x y z" # no x,y, z in the corpus

        #act
        db.get_text_centroid(text)
        # no exception => test passed
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()