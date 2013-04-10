#!/usr/bin/python
# -*- coding: utf-8 -*-
from model.logger import *

class WdNames:
    CLEAN_TEXT = 'clean_text'
    LINKS = 'links'
 

class WikiDocument(object):
    """ 
    This class represents a document from wikipedia.
    """
    def __init__(self, doc_id, title, raw_text, rev_id=None):
        self.id = doc_id
        self.title = title
        self.raw_text = raw_text 
        self.rev_id = rev_id
        self.meta = {}
        DEBUG("Created WikiDocument: {}".format(self))
    
    def __repr__(self):
        retval = """
            doc_id = {id} 
            title = {title} 
            raw_text = {raw_text} 
            rev_id = {rev_id}""".format(
                   id=self.id, 
                   title=self.title,
                   raw_text=(self.raw_text)[:80], 
                   rev_id=self.rev_id)
        return retval 
    
    def __str__(self):
        return self.__repr__()
    
        
        
        
        
        