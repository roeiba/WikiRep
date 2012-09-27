'''
Created on Sep 27, 2012

@author: roeib
'''
from stop_words_stemmer import StopWordsStemmer
import unittest
from test_utils import TestBase

class Test__StopWordStemmer(TestBase):

    def test_empty_list(self):
        text = 'a b c'
        stemmer = StopWordsStemmer([])
        
        expected = ['a','b','c']
        actual = stemmer.process_text(text)
        
        self.assertEquals(expected, actual, "error expeced={}, actual={}".format(expected,actual))
        
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    