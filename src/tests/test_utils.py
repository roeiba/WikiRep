'''
Created on Sep 27, 2012

@author: roeib
'''
import unittest
from model.stop_words_stemmer import StopWordsStemmer
from model.db_builder import DbBuilder
from model.wiki_doc import WikiDocument
from parsers import parse_tools

class TestBase(unittest.TestCase):
    def assert_almost_equals(self, expected, actual, msg=None):
        self.assertEqual(len(expected), len(actual), "dimensions mismatch")
        for i in xrange(len(expected)):
            self.assertAlmostEqual(expected[i], actual[i], msg="expected {}, actual {}".format(expected, actual) + str(msg))
        
        
class DocumentStub(object):
    id = None
    rev_id = None
    def __init__(self, title=None, raw_text=None):
        self.title = title
        self.raw_text = raw_text
        
def get_concepts_list(dump_file):
    """ 
        Generated list of Concepts from dump file
        @param dump_file: The input dump file
        @return: List of Concepts extracted from the dump
    """
    stemmer = StopWordsStemmer([])
    db_builder = DbBuilder(stemmer)
    xml_pages = parse_tools.extract_clean_pages(dump_file, keep_sections=False, keep_links=False)
    for doc_id, title, text, rev_id in xml_pages:
        doc = WikiDocument(doc_id=doc_id, title=title, raw_text=text, rev_id=rev_id)
        db_builder.add_document(doc)
    return db_builder.get_concepts_list()
    