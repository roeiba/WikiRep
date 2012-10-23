'''
Created on Oct 21, 2012

@author: roeib
'''
import unittest
import os

from model.wiki_knowledge import WikiKnowledge
from stop_words_stemmer import StopWordsStemmer

class Test(unittest.TestCase):
    def setUp(self):
        self.dump_file = os.path.abspath("wiki_knowledge_output.xml")
        self.articles = ['Southern_Cross_Expedition', 'Knowledge', 'Love', 'War']
        self.wiki_knowledge = WikiKnowledge(stemmer=StopWordsStemmer())
        self.wiki_knowledge.make_dump(self.dump_file, *self.articles, compress=False)
 
    def test__all_at_once(self):
        """ This is not exactly a test, but a program execution..."""
        self.wiki_knowledge.build(self.dump_file, None)
        self.wiki_knowledge.get_text_value("love")
#        self.wiki_knowledge.compare("i love to learn", "the world we know")
    
    
#    def test__make_dump(self):
#        pass
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