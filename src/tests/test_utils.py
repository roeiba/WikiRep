'''
Created on Sep 27, 2012

@author: roeib
'''
import unittest
from model.stop_words_stemmer import StopWordsStemmer
from model.db_builder import DbBuilder
from model.wiki_doc import WikiDocument
from model.wiki_knowledge import WikiKnowledge
from parsers import parse_tools
from model.logger import *

class TestBase(unittest.TestCase):
    def assert_almost_equals(self, expected, actual, msg=None):
        self.assertEqual(len(expected), len(actual), "dimensions mismatch")
        for i in xrange(len(expected)):
            self.assertAlmostEqual(expected[i], actual[i], msg="expected {}, actual {}".format(expected, actual) + str(msg))
        

class Factory(object):
    @staticmethod
    def build_wiki_knowledge(articles, dump_file):
        wiki_knowledge = WikiKnowledge()
        wiki_knowledge.make_dump(dump_file, *articles, compress=False)
        wiki_knowledge.build(dump_file, None)
        return wiki_knowledge

class DocumentStub(object):
    id = None
    rev_id = None
    def __init__(self, title=None, raw_text=None):
        self.title = title
        self.raw_text = raw_text

def get_db_builder(dump_file, stemmer):
    db_builder = DbBuilder(stemmer)
    xml_pages = parse_tools.extract_clean_pages(dump_file, keep_sections=False, keep_links=False)
    for doc_id, title, text, rev_id in xml_pages:
        doc = WikiDocument(doc_id=doc_id, title=title, raw_text=text, rev_id=rev_id)
        db_builder.add_document(doc)
    return db_builder
    
def get_concepts_list(dump_file):
    """ 
        Generated list of Concepts from dump file
        @param dump_file: The input dump file
        @return: List of Concepts extracted from the dump
    """
    stemmer = StopWordsStemmer([])
    return get_db_builder(dump_file, stemmer).get_concepts_list()

# - - - - - Messages and formats - - - - - - - 

CORRELATION_MESSAGE = """
        Text 1: {text1}
        Text 2: {text2}
        Correlation : {correlation}  
        """
        
def get_texts_correlation_message(text1, text2, correlation):
    return CORRELATION_MESSAGE.format(
         text1 = log_text(text1), 
         text2 = log_text(text2),
         correlation = correlation)
    
VALUE_MESSAGE = """
        Text: {text}
        Vector : {text_value}  
        """
        
def get_text_value_message(text, text_value):
    return VALUE_MESSAGE.format(
     text = log_text(text), 
     text_value = text_value)
        