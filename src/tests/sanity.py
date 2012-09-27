'''
Created on Sep 19, 2012
'''
import semantic_interpreter

import unittest
import numpy as np
from collections import namedtuple


#model
from stop_words_stemer import StopWordsSteemer


DataBaseWrapperStub = namedtuple('DdWrapperStub','word_index concept_index wieght_matrix')


class Test__SemanticInterpiter(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def getSimpleDb(self):
        db = DataBaseWrapperStub(
            word_index=['a','b','c'],
            concept_index=['c1','c2'],
            wieght_matrix=np.matrix(
              [[0.5, 0.5],
               [0.2, 0.8],
               [1.0, 0.0]])
        ) 
        return db   

# ------------------------   Tests -----------------------------------

    def test_Init(self):
        # arrange
        db = self.getSimpleDb()
        
        # act
        semantic_interpreter.SemanticInterpreter(db,StopWordsSteemer([]))
        

    def test_Build(self):
        # arrange
        db = self.getSimpleDb()
        
        text = "a b c"
        
        steemer = StopWordsSteemer([])
        si = semantic_interpreter.SemanticInterpreter(db,steemer)
                
        # act
        w  = si.build_weighted_vector(text)
        print w

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()