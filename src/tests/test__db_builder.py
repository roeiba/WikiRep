'''
Created on Sep 28, 2012

@author: roeib
'''
import unittest
from db_builder import DbBuilder
from stop_words_stemmer import StopWordsStemmer
import test_utils

class DocumentStub(object):
    raw_text = None 
    title = None
    
class Test(test_utils.TestBase):
    def setUp(self):
        stemmer = StopWordsStemmer([])
        self.db_builder = DbBuilder(stemmer)
        
        
    def test__single_doc(self):
        doc = DocumentStub()
        doc.title = "Testing"
        doc.raw_text = "The eagle has landed"
        self.db_builder.add_document(doc)
        
        expected_titles_index = ["Testing"]
        expected_words_index = ["The", "eagle", "has", "landed"]
        expceted_wieghts_matrix = [ [0], [0], [0], [0] ]
        
        #create db
        actual_db = self.db_builder.build()
        self.assert_dbs_equal(actual_db, expected_titles_index, expected_words_index, expceted_wieghts_matrix)
        
        
        
    def assert_dbs_equal(self, actual_db, expected_titles_index, expected_words_index, expceted_wieghts_matrix):
        #validate results
        self.assertEqual(set(actual_db.words_index), set(expected_words_index), "Mismatch words index content (not validating order)")
        self.assertEqual(actual_db.get_titles_index(), expected_titles_index, "Mismatch concepts index")
        
        #validate db_matrix content
        for j in range(len(expected_titles_index)):
            for i in range(len(expected_words_index)):
                title = expected_titles_index[j]
                #extract expected values from index and matrix
                expected_word = expected_words_index[i]
                expected_wieght = expceted_wieghts_matrix[i][j]
                
                actual_word_index = actual_db.words_index.index(expected_word)
                actual_concept_index = actual_db.get_titles_index().index(title)
                actual_wieght = actual_db.wieght_matrix[actual_word_index][actual_concept_index]
                self.assertAlmostEqual(expected_wieght, actual_wieght, "Wrong table value at [{}, {}]".format(expected_word, title))
                
                
    def test__parsing_fails_on_duplicated_title(self):
        pass
    
        

if __name__ == "__main__":
    unittest.main()
    
    #\nThe bird have fallen\nWhy do birds suddenly appear?"