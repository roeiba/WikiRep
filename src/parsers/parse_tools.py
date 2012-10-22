'''
Created on Oct 15, 2012

@author: inesmeya
'''

import xml.etree.ElementTree as etree
import parsers.web_tools as wt
import gzip

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

def parse(filename): 
    if filename.endswith(".gzip"):
        filename = gzip.open(filename)
    return etree.parse(filename)
    