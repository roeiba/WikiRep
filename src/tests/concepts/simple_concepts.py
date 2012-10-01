# -*- coding: utf-8 -*-

from model.concept import Concept
import unittest
from tests import test_utils
from model import db_builder
from model.stop_words_stemmer import StopWordsStemmer
concepts = [
      
    Concept(1, "Technology", 
    [
         'computer', 'technology', 'system',
         'service',  'site',       'phone', 
         'internet', 'machine' 
    ]),
           
    Concept(2, "Business",
    [
        'store', 'product', 'sales', 'sell',
        'business', 'advertising','market', 
        'consumer'
    ]),
    
    Concept(3, "Entertainment",
    [            
        'play', 'film', 'production', 
        'movie', 'theater', 'stage'
        'star', 'director', 
    ])
        
] # end of concepts
        

class TestSimpleConcepts(test_utils.TestBase):
    
    def test_print(self):
        builder = db_builder.DbBuilder(StopWordsStemmer())
        
        #HACK:
        for c in concepts:
            builder.concepts_list.append(c)
            
        db = builder.build()
        
        print db.words_index
        print db.get_titles_index()
        print db.wieght_matrix
        
        
            
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()