#!/usr/bin/python
# -*- coding: utf-8 -*-
from model.logger import *
import xml.etree.ElementTree as etxml
import StringIO

class WdNames:
    CLEAN_TEXT = 'clean_text'
    LINKS = 'links'

def doc_from_xml(doc_tag):
    doc = doc_tag.attributs
    return WikiDocument(doc.id ,doc.title, doc_tag.text, doc.rev_id) 

def wiki_doc_to_xml(wiki_doc):
    '''@param WikiDocument param:
       @return: String in xml format, represenation 
    '''
    el_doc = etxml.Element('doc')
    el_doc.attrib['id']=str(wiki_doc.id)
    el_doc.attrib['title']=wiki_doc.title
    el_doc.attrib['rev_id']=str(wiki_doc.rev_id)
    el_doc.text = wiki_doc.clean_text
    output = StringIO.StringIO()
    etxml.ElementTree(el_doc).write(output)
    
    string = output.getvalue() + "\n"
    output.close()
    return string


class WikiDocument(object):
    """ 
    This class represents a document from wikipedia.
    """
    def __init__(self, doc_id, title, wiki_text, rev_id=None):
        self.id = doc_id
        self.title = title
        self.wiki_text = wiki_text 
        self.rev_id = rev_id
        self.meta = {}
        self.clean_text = None
        DEBUG("Created WikiDocument: {}".format(self))
    
    def __repr__(self):
        retval = """
            doc_id = {id} 
            title = {title} 
            wiki_text = {wiki_text} 
            rev_id = {rev_id}""".format(
                   id=self.id, 
                   title=self.title,
                   wiki_text=(self.wiki_text)[:80], 
                   rev_id=self.rev_id)
        return retval 
    
    def __str__(self):
        return self.__repr__()
    
        
        
        
        
        
