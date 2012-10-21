'''
Created on Oct 21, 2012

@author: roeib
'''
import unittest
from model.wiki_knowledge import WikiKnowledge


class Test(unittest.TestCase):
    def setUp(self):
        self.wiki_knowledge = WikiKnowledge()
        #TODO: init wiki properly
 
    def test__make_dump(self):
        pass
    
    def test__download(self):
        pass
    
    def test__parse(self):
        pass
    def test__build(self):
        pass
    def test__compare(self):
        pass
    def test__get_text_value(self):
        pass
    def test__analize(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()