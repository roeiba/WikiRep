'''
Created on Oct 15, 2012

@author: inesmeya
'''

import xml.etree.ElementTree as etree
import parsers.web_tools as wt
import WikiExtractor 
import gzip
from model.logger import *

_PAGE_TAG = wt.mk_tag('page')


def my_xfind(doc, xp):
    new_xp = xp.replace('/', '/{{{}}}'.format(wt._NS))
    return doc.find(new_xp)
    

def extract_pages(f):
    """Extract pages from Wikimedia database dump.

    Parameters
    ----------
    f : file-like or str
        (Path to) a file containing a page dump in XML format; e.g.
        <lang>wiki-<data>-pages-articles.xml.

    Returns
    -------
    pages : iterable over (int, str, str)
        Generates (page_id, title, content) triples.
    """
    
    # get an iterable
    if f.endswith(".gzip"):
        f = gzip.open(f)
    context = etree.iterparse(f, events=["end"], parser=etree.XMLParser(encoding='utf-8'))
    
    # turn it into an iterator
    context = iter(context)
    
    # get the root element
    event, root = context.next()
    
    for event, elem in context:     
        if event == "end" and elem.tag == _PAGE_TAG:
            tid    = my_xfind(elem,'./id').text
            title  = my_xfind(elem,'./title').text
            text   = my_xfind(elem,'./revision/text').text   
            rev_id = my_xfind(elem,'./revision/id').text         
            
            yield (tid, title, text,rev_id)
            
            elem.clear()     
            root.clear()

def extract_clean_pages(src_wiki_dump, keep_sections=False,keep_links=False):
    """ Wrapper for extract_pages that output clean text according to parameters
    @param keep_sections: preserve sections
    @param keep_links: preserve links
    """
    for tid, title, text, rev_id in extract_pages(src_wiki_dump):
        clean_text =  WikiExtractor.clean(text)
        DEBUG("""
        Original text:
        {separator} Start {separator}
        {text} 
        {separator} END {separator}
        Clean text:
        {separator} Start {separator}
        {clean_text}
        {separator} END {separator} 
        """.format(separator = "-"*20, text=log_text(text) , clean_text=log_text(clean_text)))
        yield tid, title, clean_text, rev_id
        
        
def parse(filename): 
    if filename.endswith(".gzip"):
        filename = gzip.open(filename)
    return etree.parse(filename)
    