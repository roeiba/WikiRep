'''
Created on Sep 27, 2012

@author: roeib
'''
import unittest
from model.stemmers import StopWordsStemmer
from model.db_builder import DbBuilder
#from model.wiki_doc import WikiDocument
import wiki_knows.wiki_knowledge as wiki_knowledge
from parsers import parse_tools
#from model.logger import *
from parsers import WikiExtractor 

class TestBase(unittest.TestCase):
    pass


class DocumentStub(object):
    id = None
    rev_id = None
    def __init__(self, title=None, raw_text=None):
        self.title = title
        self.raw_text = raw_text
        self.wiki_text = raw_text
        self.clean_text = raw_text


def get_db_builder(dump_file, stemmer):
    db_builder = DbBuilder(stemmer)
    clean_docs = parse_tools.iterate_clean_pages(dump_file, WikiExtractor.clean)#    (dump_file, keep_sections=False, keep_links=False)
    for doc in clean_docs:
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
         text1 = (text1)[:80], 
         text2 = (text2)[:80],
         correlation = correlation)
    
VALUE_MESSAGE = """
        Text: {text}
        Vector : {text_value}  
        """
        
def get_text_value_message(text, text_value):
    return VALUE_MESSAGE.format(
     text = (text)[:80], 
     text_value = text_value)
        