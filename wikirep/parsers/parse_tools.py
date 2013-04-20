import xml.etree.ElementTree as etree
#import parsers.web_tools as wt
import web_tools as wt

import WikiExtractor 
import gzip
from  model.wiki_doc import WikiDocument
from  model.wiki_doc import doc_from_xml, WdNames, wiki_doc_to_xml
from parsers.wikitext_processor import  WikiTextProcessor

import logging
from numpy.distutils.from_template import item_re
_log = logging.getLogger(__name__)

# for log purpurses
def _cut_text(text):
    ''' text will be cut to fit screen'''
    return text[:80] + "... total chars {}".format(len(text))

# wikipage = retrive_page(i)
# WikiDoc =  doc_to(wikipage)
# StemedDump = retrive_page(i)


_PAGE_TAG = wt.mk_tag('page')
_DOC_TAG = 'doc'

def my_xfind(doc, xp):
    new_xp = xp.replace('/', '/{{{}}}'.format(wt._NS))
    return doc.find(new_xp)
    
def doc_from_wikipagexml(page_tag):
    tid    = my_xfind(page_tag,'./id').text
    title  = my_xfind(page_tag,'./title').text
    text   = my_xfind(page_tag,'./revision/text').text   
    rev_id = my_xfind(page_tag,'./revision/id').text         
    
    wikidoc = WikiDocument(int(tid), title, text,int(rev_id))

    
    _log.info("element proceeded: {}".format(wikidoc.title) )
    return wikidoc



def cleaner_WikiTextProcessor(wikidoc):
    wp = WikiTextProcessor(wikidoc.wiki_text)
    #wdoc.raw_text = wp.get_clean_text()
    wikidoc.clean_text = wp.get_text_only()
    wikidoc.meta[WdNames.LINKS] = wp.get_links()
    return wikidoc

def cleaner_WikiExtractor(wikidoc):
    wikidoc.clean_text = WikiExtractor.clean(wikidoc.wiki_text)
    return wikidoc


def iterate_clean_pages(f,clean_tarnform):
    pages = iterate_xml(f, _PAGE_TAG)
    return gen_apply(pages, doc_from_wikipagexml, clean_tarnform)

def iterate_wiki_pages(f):
    pages = iterate_xml(f, _PAGE_TAG)
    return gen_apply(pages, doc_from_wikipagexml)

# load xml of parsed dumeb repr
def iterate_wiki_doc(f):
    docs = iterate_xml(f, _DOC_TAG)
    return gen_apply(docs, doc_from_xml)    

def gen_apply(source, *ftransforms):
    '''applyse to source transformations
    @return: result of pipe
    '''
    for element in source:
        result = element
        for ftransform in ftransforms:
            result = ftransform(result)
        yield result
    
def iterate_xml(f,tag_name):
    """Itarage overs list of xlm tags (wiht tag_name),
    from stream/f. every tag content yields out.
    
    @param file-like or str:  path to  wiki xmldump, or stream, it contains
    @requires: iterable over xml element in wikipedia fromat
    @yeilds tags w
    """
    
    context = etree.iterparse(f, events=["end"], parser=etree.XMLParser(encoding='utf-8'))
    context = iter(context)       # turn it into an iterator
    
    # this is not get us the root, but the first element
    #TODO: investigate
    #event, root = context.next()  #get the root element
    
    for event, elem in context:     
        if event == "end" and elem.tag == tag_name:
            yield elem           
            elem.clear()     
            #root.clear()
'''

#--------------------------------------------------------


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
        Generates (page_id, title, content, revision_id) triples.
    """
    
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
            
            wk_doc = WikiDocument(int(tid), title, text,int(rev_id))
            
            _log.info("page extracted: {}".format(title) )
            yield wk_doc
            
            elem.clear()     
            root.clear()

def extract_clean_pages(src_wiki_dump, keep_sections=False,keep_links=False):
    """ Wrapper for extract_pages that output clean text according to parameters
    @param keep_sections: preserve sections
    @param keep_links: preserve links
    """
    for wdoc in extract_pages(src_wiki_dump):
        tid, title, text, rev_id = wdoc.id, wdoc.title, wdoc.raw_text, wdoc.rev_id
        clean_text =  WikiExtractor.clean(text)
        
        _log.debug("""
        Original text:
        {separator} Start {separator}
        {text} 
        {separator} END {separator}
        Clean text:
        {separator} Start {separator}
        {clean_text}
        {separator} END {separator} 
        """.format(separator = "-"*20, 
                   text=_cut_text(text) , 
                   clean_text=_cut_text(clean_text))
        )
        
        yield tid, title, clean_text, rev_id
        
'''        
def parse_xml(filename): 
    if filename.endswith(".gzip"):
        filename = gzip.open(filename)
    return etree.parse(filename)


            
