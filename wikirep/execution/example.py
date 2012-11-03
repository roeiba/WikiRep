'''
Created on Oct 21, 2012

@author: roeib
'''
import unittest
import os

from model.wiki_knowledge import WikiKnowledge
from stop_words_stemmer import StopWordsStemmer
from model.logger import *
from tests import test_utils

class Test(unittest.TestCase):
    def setUp(self):
        self.dump_file = os.path.abspath("wiki_knowledge_output.xml")
        
    def test__execution(self):
        """ This is not exactly a test, but a program execution..."""
        articles = ['Southern_Cross_Expedition', 'Knowledge', 'Love', 'War', 'Hypertext_Transfer_Protocol'
                        'Government', 'Peace', 'Fame', 'Shame', 'School', 'Cat', 'Dog', 'House']
        text1 = "i love to learn"
        text2 = "the world we know"
        wiki_knowledge = test_utils.Factory.build_wiki_knowledge(articles, self.dump_file)
        correlation = wiki_knowledge.compare(text1, text2)
        INFO(test_utils.get_texts_correlation_message(text1, text2, correlation))
    
    def test__cat_example(self):
        articles = ['Cat', "Feline", "Pet", "Mouse", "Tom_and_Jerry", 'Dog', 'Cats_and_Dogs', 'Southern_Cross_Expedition',
                         'Knowledge', 'Love', 'War', 'Hypertext_Transfer_Protocol'
                        'Government', 'Peace', 'Fame', 'Shame', 'School']
        text = "Cat"
        wiki_knowledge = test_utils.Factory.build_wiki_knowledge(articles, self.dump_file)
        text_value = wiki_knowledge.get_text_value(text)
        INFO(test_utils.get_text_value_message(text, text_value))

#    
#    def test__download(self):
#        pass
#    
#    def test__parse(self):
#        pass
#    def test__build(self):
#        pass
#    def test__compare(self):
#        pass
#    def test__get_text_value(self):
#        pass
#    def test__analize(self):
#        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
