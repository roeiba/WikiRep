'''
Created on Sep 28, 2012

@author: roeib
'''
import unittest
from model.db_builder import DbBuilder
from model.stemmers import StopWordsStemmer
import test_utils
import math

    
class Test(test_utils.TestBase):
    def setUp(self):
        stemmer = StopWordsStemmer([])
        self.db_builder = DbBuilder(stemmer)
        
    def test__simple_doc(self):
        doc = test_utils.DocumentStub(title = "Testing",raw_text = "The eagle has landed")
        self.db_builder.add_document(doc)
        
        expected_titles_index = ["Testing"]
        expected_words_index = ["The", "eagle", "has", "landed"]
        expceted_wieghts_matrix = [ [0], [0], [0], [0] ]
        
        #create db
        actual_db = self.db_builder.build()
        self.assert_dbs_equal(actual_db, expected_titles_index, expected_words_index, expceted_wieghts_matrix)
    
    def tfidf(self, counter):
        return (1 + math.log(counter)) if counter else 0
     
    def test__advanced_doc(self):
        #first doc
        doc = test_utils.DocumentStub(title = "Testing advanced",raw_text = "a b c c c d d d d e")
        self.db_builder.add_document(doc)

        #second doc
        doc = test_utils.DocumentStub(title = "Testing advanced 2",raw_text = "a a a a a b c c c d d d e e")
        self.db_builder.add_document(doc)
        
        #third doc
        doc = test_utils.DocumentStub(title = "Testing advanced 3",raw_text = "b b b b f f f f")
        self.db_builder.add_document(doc)
        
        docs_num = 3
        expected_titles_index = ["Testing advanced", "Testing advanced 2", "Testing advanced 3"]
        expected_words_index = ['a', 'b', 'c', 'd', 'e', 'f']
        wieghts_matrix = [ 
            [self.tfidf(counter) * math.log(docs_num / 2.0) for counter in [1, 5, 0]], #a 
            [self.tfidf(counter) * math.log(docs_num / 3.0) for counter in [1, 1, 4]], #b 
            [self.tfidf(counter) * math.log(docs_num / 2.0) for counter in [3, 3, 0]], #c 
            [self.tfidf(counter) * math.log(docs_num / 2.0) for counter in [4, 3, 0]], #d 
            [self.tfidf(counter) * math.log(docs_num / 2.0) for counter in [1, 2, 0]], #e 
            [self.tfidf(counter) * math.log(docs_num / 1.0) for counter in [0, 0, 4]], #f 
            ]
        
        #cosine normalization
        expceted_wieghts_matrix = []
        for row in wieghts_matrix:
            norm = math.sqrt( sum([t**2 for t in row]) )
            normalized_row = [norm * t for t in row]
            expceted_wieghts_matrix.append(normalized_row)
            
        #create db
        actual_db = self.db_builder.build()
        self.assert_dbs_equal(actual_db, expected_titles_index, expected_words_index, wieghts_matrix)
        
        #TODO: use the normalized matrix for comparison once db_builder supports normalization
        #self.assert_dbs_equal(actual_db, expected_titles_index, expected_words_index, expceted_wieghts_matrix)
        
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
                actual_wieght = actual_db.wieght_matrix[actual_word_index,actual_concept_index]
                self.assertAlmostEqual(expected_wieght, actual_wieght, msg="Wrong table value at word/concept [{}, {}]".format(expected_word, title))
                
                
    def test__parsing_fails_on_duplicated_title(self):
        pass
    
        

if __name__ == "__main__":
    unittest.main()
    
    #\nThe bird have fallen\nWhy do birds suddenly appear?"