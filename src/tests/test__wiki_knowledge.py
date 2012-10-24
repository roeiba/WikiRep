'''
Created on Oct 21, 2012

@author: roeib
'''
import unittest
import os

from model.wiki_knowledge import WikiKnowledge
from stop_words_stemmer import StopWordsStemmer
from model.logger import *

class Test(unittest.TestCase):
    def setUp(self):
        self.dump_file = os.path.abspath("wiki_knowledge_output.xml")
        self.correlation_message = """
        Text 1: {text1}
        Text 2: {text2}
        Correlation : {correlation}  
        """
        self.value_message = """
        Text: {text}
        Vector : {text_value}  
        """
    
    def _build_wiki_knowledge(self, articles):
        self.wiki_knowledge = WikiKnowledge()
        self.wiki_knowledge.make_dump(self.dump_file, *articles, compress=False)
        self.wiki_knowledge.build(self.dump_file, None)
        
    def _get_texts_correlation(self, text1, text2):
        correlation = self.wiki_knowledge.compare(text1, text2)
        INFO(self.correlation_message.format(
             text1 = log_text(text1), 
             text2 = log_text(text2),
             correlation = correlation))
    
    def _get_text_value(self, text):
        text_value = self.wiki_knowledge.get_text_value(text)
        INFO(self.value_message.format(
             text = log_text(text), 
             text_value = text_value))
        
    def test__execution(self):
        """ This is not exactly a test, but a program execution..."""
        articles = ['Southern_Cross_Expedition', 'Knowledge', 'Love', 'War', 'Hypertext_Transfer_Protocol'
                        'Government', 'Peace', 'Fame', 'Shame', 'School', 'Cat', 'Dog', 'House']
        text1 = "i love to learn"
        text2 = "the world we know"
        self._build_wiki_knowledge(articles)
        self._get_texts_correlation(text1, text2)
    
    def test__cat_example(self):
        articles = ['Cat', "Feline", "Pet", "Mouse", "Tom_and_Jerry", 'Dog', 'Cats_and_Dogs', 'Southern_Cross_Expedition',
                         'Knowledge', 'Love', 'War', 'Hypertext_Transfer_Protocol'
                        'Government', 'Peace', 'Fame', 'Shame', 'School']
        self._build_wiki_knowledge(articles)
        self._get_text_value("Cat")
        self._get_text_value("cat")

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
