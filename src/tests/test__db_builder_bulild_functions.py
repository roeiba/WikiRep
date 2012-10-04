'''
Created on Sep 28, 2012

@author: inesmeya
'''
import unittest
import model.build_utils as dbb
from model.concept import Concept

class Test__DbBuilderPrivates(unittest.TestCase):

    def test_build_index_by_words_not_empty(self):
        word_list = ['a', 'd', 'b']
        expected = { 'a': 0, 'd':1, 'b':2}
        actual = dbb.build_index_by_words(word_list)
        self.assertEqual(expected, actual)
        
    def test_build_index_by_wordsempty(self):
        word_list = []
        expected = {}
        actual = dbb.build_index_by_words(word_list)
        self.assertEqual(expected, actual)    

    def test_bulid_word_index(self):
        concepts_list = [
            Concept(0, 'title0', ['a', 'b', 'c']),
            Concept(1, 'title1', ['b', 'c']),
            Concept(2, 'title2', ['x', 'c']),
            ]
        
        expected =['a', 'b', 'c', 'x']
        actual = dbb.bulid_word_index(concepts_list)
        
        self.assertEqual(set(expected), set(actual))    

    def test_bulid_word_index_empty(self):
        expected =[]
        actual = dbb.bulid_word_index([])
        
        self.assertEqual(expected, actual) 
   
    def test_build_df(self):
        concepts_list = [
            Concept(0, 'title0', ['a', 'b', 'c']),
            Concept(1, 'title1', ['b', 'c']),
            Concept(2, 'title2', ['x', 'c']),
            ]
        index_by_word={'a':0, 'b':1, 'c':2, 'x':3 }
                
        expected =[1,2,3,1]
        actual = dbb.build_df(index_by_word,concepts_list)
        self.assertEqual(expected, actual) 



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()