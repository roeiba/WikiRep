'''
Created on Oct 21, 2012

@author: roeib
'''
import unittest
import os

from wiki_knows import wiki_knowledge 
from model.stemmers import StopWordsStemmer
from parsers import parse_tools
from model.logger import *
import test.test_utils as test_utils
from io_test_utils import getOutputFile
from model import semantic_interpreter

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

        dump_file = self.tmp_dump_file

        wiki_knowledge.make_dump(dump_file, self.expected_articles, compress=False)
        pparsed_xml_path = dump_file +".parsed"
        wiki_knowledge.parse_dump(dump_file, pparsed_xml_path)
        db_wrapper = wiki_knowledge.build_database_wrapper(pparsed_xml_path, StopWordsStemmer([]))
                             
        #wiki_knowledge = test_utils.Factory.build_wiki_knowledge()
        #clean up file created by factory at end
        self.addCleanup(os.remove, self.tmp_dump_file)
        
        comparer = semantic_interpreter.SemanticComparer(db_wrapper)
        correlation = comparer.compare(text1, text2)
        INFO(test_utils.get_texts_correlation_message(text1, text2, correlation))
    
    def test__make_dump(self):
        #create the dump file
        article_title=["Rain"]
        articles_expected_set = set(article_title)
        wiki_knowledge.make_dump(self.tmp_dump_file,article_title)
        
        actual_titles_set = {wikidoc.title for wikidoc in parse_tools.iterate_wiki_pages(self.tmp_dump_file)}
        self.assertEqual(actual_titles_set, articles_expected_set, "title mismatch")

        
    def test__parse_dumps_to_cocepts(self):
        self.skipTest("Implement this test!")
        test_utils.get_db_builder(self.expected_xml_path)
        
    def test__save_and_load(self):
        parsed_xml =self.expected_xml_path + ".parsed"
        wiki_knowledge.parse_dump(self.expected_xml_path, parsed_xml)
        expected_db = wiki_knowledge.build_database_wrapper(parsed_xml, StopWordsStemmer([]))
        wiki_knowledge.save_db_wrapper_to_wdb(expected_db, self.tmp_wdb_file)                
        actual = wiki_knowledge.load_db_wrapper_from_wdb(self.tmp_wdb_file) 
        self.assertEqual(expected_db.words_num, actual.words_num, "Mismatch WikiKnowledges number of words")
        self.assertEqual(expected_db.title_index, actual.title_index, "Mismatch WikiKnowledges titles")
        
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
