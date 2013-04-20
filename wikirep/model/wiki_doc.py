#!/usr/bin/python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as etxml
import StringIO

from model.logger import getLogger
_log = getLogger(__name__)

class WdNames:
    CLEAN_TEXT = 'clean_text'
    LINKS = 'links'

def doc_from_xml(doc_tag):
    doc = doc_tag.attrib
    wd = WikiDocument(doc['id'] ,doc['title'], None, doc['rev_id'], clean_text=doc_tag.text) 
    return wd

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
    Currently is half baked object, since it used on 
        1. wiki parsed  doc construction: then clean_text = None
        2. wiki cleaned doc: when wiki_text transformed to normal text
    When loaded from xml parsed dump file, wiki_text == None
    """
    def __init__(self, doc_id, title, wiki_text, rev_id=None, clean_text = None):
        self.id = doc_id
        self.title = title
        self.wiki_text = wiki_text 
        self.rev_id = rev_id
        self.meta = {}
        self.clean_text = clean_text
        _log.debug("Created WikiDocument: {}".format(self))
    
    def __repr__(self):
        retval = "{title}:{id}".format(id=self.id, title=self.title)
        return retval 
        
    def __str__(self):
        return self.__repr__()
    
        
        
        
        
        
