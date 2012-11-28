'''
Created on Oct 21, 2012

@author: roeib
'''
import unittest
import os

from model.wiki_knowledge import WikiKnowledge
from model.stop_words_stemmer import StopWordsStemmer
from model.logger import *
import test.test_utils as test_utils
from io_test_utils import getOutputFile

class Test(unittest.TestCase):
    def setUp(self):
        self.tmp_dump_file = getOutputFile("wiki_knowledge_output.xml")
        self.tmp_wdb_file = getOutputFile("wiki_knowledge_output.wdb")
        
        self.expected_articles = ['Knowledge', 'Love', 'War'] 
        self.expected_xml_path = os.path.join(os.path.dirname(__file__) ,"expected_results/expected_xml_Knowledge_Love_War.xml")
        self.expected_wdb_path = os.path.join(os.path.dirname(__file__) ,"expected_results/expected_Knowledge_Love_War.wdb")
        
    def tearDown(self):
        pass
        
    def test__execution(self):
        """ This is not exactly a test, but a program execution..."""
        text1 = "i love to learn"
        text2 = "the world we know"
        wiki_knowledge = test_utils.Factory.build_wiki_knowledge(self.expected_articles, self.tmp_dump_file)
        #clean up file created by factory at end
        self.addCleanup(os.remove, self.tmp_dump_file)
        correlation = wiki_knowledge.compare(text1, text2)
        INFO(test_utils.get_texts_correlation_message(text1, text2, correlation))
    
    def test__make_dump(self):
        #create the dump file
        test_utils.Factory.build_wiki_knowledge(self.expected_articles, self.tmp_dump_file)
        
        #compare with expected
        with open(self.expected_xml_path) as exp:
            with open(self.tmp_dump_file) as act:
                expected = exp.readlines()
                actual =  act.readlines()
                self.assertEqual(expected, actual, "Mismatch dumps")
    
    def test__parse_dumps_to_cocepts(self):
        self.skipTest("Implement this test!")
        test_utils.get_db_builder(self.expected_xml_path)
        
    def test__save_and_load(self):
        self.skipTest("Until save and load is implemented")
        wiki_knowledge = WikiKnowledge()
        wiki_knowledge.build(self.expected_xml_path, None)      
        wiki_knowledge.save_to_disk(self.tmp_wdb_file)
        with open(self.tmp_wdb_file) as act:
            with open(self.expected_wdb_path) as exp:
                expected = exp.readlines()
                actual =  act.readlines()
                self.assertEqual(expected, actual, "Mismatch dumps")
        
        loaded_wiki_knowledge = WikiKnowledge()
        loaded_wiki_knowledge.load(self.wdb_file)
        self.assertEqual(wiki_knowledge, loaded_wiki_knowledge, "Mismatch WikiKnowledges")
        
    def test__run_from_dump(self):
        pass
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
