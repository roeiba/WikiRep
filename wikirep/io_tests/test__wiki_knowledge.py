'''
Created on Nov 28, 2012

@author: inesmeya
'''
import unittest
import model.wiki_knowledge as mwn
import io_test_utils as io_tu





class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test__parse_dump(self):
        wn = mwn.getWikiKnowledge()
        wiki_dump_path =  io_tu.getInputFile(io_tu.FilesList.test__parse_tools)
        wiki_parsed_dump_path =  io_tu.getOutputFile(io_tu.FilesList.test__parse_tools)
        
        wn.parse_dump(wiki_dump_path, wiki_parsed_dump_path)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test__parse_dump']
    unittest.main()