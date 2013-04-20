import unittest
import wiki_knows.wiki_knowledge as wn
import io_tests.io_test_utils as io_tu
from model.stemmers import StopWordsStemmer
from model.semantic_interpreter import SemanticComparer

import test.test_utils as test_utils
from io_test_utils import getOutputFile, getInputFile

import os

from model.logger import getTestLogger
_log = getTestLogger("Test")

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test__parse_dump(self):
        wiki_dump_path =  io_tu.getInputFile(io_tu.FilesList.test__parse_tools)
        wiki_parsed_dump_path =  io_tu.getOutputFile(io_tu.FilesList.test__parse_tools)
      
        wn.parse_dump(wiki_dump_path, wiki_parsed_dump_path)


    def test_number_of_concepts(self):
        """ db builder reads parsed xml properly"""
        
        _log.info('-'*80)
        
        # arrange 
        dump_file = getInputFile("wikidump_Knowledge_Love_War.xml")
        parsed_file = getOutputFile("wikidump_Knowledge_Love_War.parsed.xml")
        
        # act
        wn.parse_dump(dump_file, parsed_file)
        db_wrapper = wn.build_database_wrapper(parsed_file, StopWordsStemmer([]))
        
        titles_count =len(db_wrapper.title_index)
        concepts_count =len(db_wrapper.concepts_index)
        
        # assert
        self.assertEqual(titles_count, 3, "number of tiltes should be 3, got {0}".format(titles_count))                     
        self.assertEqual(concepts_count, 3, "number of tiltes should be 3, got {0}".format(concepts_count)) 
    
    def test__same_text_correlation(self):
        """ Test that for same text correlation is 1"""
        
        _log.info('-'*80)
        
        # arrange 
        text1 = "love is rain as long story short"
        text2 = text1

        dump_file = getOutputFile("swiki_knowledge_output.xml")
        parsed_file = getOutputFile("swiki_knowledge_output.parsed.xml")
        #wdb_file = getOutputFile("swiki_knowledge_output.wdb")

        articles = ['Rain', 'Love', 'Tree'] 
        
        # act
        wn.make_dump(dump_file, articles, compress=False)
        wn.parse_dump(dump_file, parsed_file)
        db_wrapper = wn.build_database_wrapper(parsed_file, StopWordsStemmer([]))
                             
        #self.addCleanup(os.remove, self.tmp_dump_file)
        
        comparer = SemanticComparer(db_wrapper)
        correlation = comparer.compare(text1, text2)
        _log.info(test_utils.get_texts_correlation_message(text1, text2, correlation))
        self.assertAlmostEqual(correlation, 1.0, msg="for same text correlation should be 1")
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test__parse_dump']
    unittest.main()