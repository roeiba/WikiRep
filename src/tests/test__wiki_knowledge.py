'''
Created on Oct 21, 2012

@author: roeib
'''
import unittest
import os

from model.wiki_knowledge import WikiKnowledge
from stop_words_stemmer import StopWordsStemmer
from model.logger import *
import test_utils

class Test(unittest.TestCase):
    def setUp(self):
        self.tmp_dump_file = os.path.abspath("wiki_knowledge_output.xml")
        self.expected_articles = ['Knowledge', 'Love', 'War'] 
        self.expected_result_path = os.path.join(os.path.dirname(__file__) ,"expected_results/expected_xml_Knowledge_Love_War.xml")
        
    def tearDown(self):
        os.remove(self.tmp_dump_file)
        
    def test__execution(self):
        """ This is not exactly a test, but a program execution..."""
        text1 = "i love to learn"
        text2 = "the world we know"
        wiki_knowledge = test_utils.Factory.build_wiki_knowledge(self.expected_articles, self.tmp_dump_file)
        correlation = wiki_knowledge.compare(text1, text2)
        INFO(test_utils.get_texts_correlation_message(text1, text2, correlation))
    
    def test__make_dump(self):
        wiki_knowledge = test_utils.Factory.build_wiki_knowledge(self.expected_articles, self.tmp_dump_file)
        
        with open(self.expected_result_path) as exp:
            with open(self.tmp_dump_file) as act:
                expected = exp.readlines()
                actual =  act.readlines()
                self.assertEqual(expected, actual, "Mismatch dumps")
            
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
