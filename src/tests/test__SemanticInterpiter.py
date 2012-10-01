'''
Created on Sep 19, 2012
'''
from model import semantic_interpreter
import unittest
import numpy as np
from test_utils import TestBase
 
#model
from model.stop_words_stemmer import StopWordsStemmer

class Test__SemanticInterpiter(TestBase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def getSimpleDb(self):
        concepts_index=['c1','c2']
        words_index=['a','b','c']
        wieght_matrix =np.array(
              [[0.5, 0.5],
               [0.2, 0.8],
               [1.0, 0.0]])
        print type(wieght_matrix)
        db = semantic_interpreter.DatabaseWrapper( wieght_matrix, concepts_index, words_index)
        return db

# ------------------------   Tests -----------------------------------

    def test_init(self):
        # arrange
        db = self.getSimpleDb()
        
        # act
        semantic_interpreter.SemanticInterpreter(db, StopWordsStemmer([]))
        

    def test_simple(self):
        # arrange
        db = self.getSimpleDb()
        
        text = "a b c"
        stemmer = StopWordsStemmer([])
        si = semantic_interpreter.SemanticInterpreter(db, stemmer)
           
        expected = np.array([1.7/3, 1.3/3])
        # act
        actual  = si.build_weighted_vector(text)
        self.assert_almost_equals(expected, actual, "wrong centroid")
        
    def test_words_not_in_corpus(self):
        # arrange
        db = self.getSimpleDb()
        
        text = "x y z"
        stemmer = StopWordsStemmer([])
        si = semantic_interpreter.SemanticInterpreter(db, stemmer)
           
        # expected = np.array([1.7/3, 1.3/3])
        # 
        actual  = si.build_weighted_vector(text)
        #self.assert_almost_equals(expected, actual, "wrong centroid")
        
                 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()