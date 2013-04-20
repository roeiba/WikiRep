import xml.etree.ElementTree as etree
import gzip

import WikiExtractor 
from parsers.wikitext_processor import  WikiTextProcessor

from  model.wiki_doc import WikiDocument
from  model.wiki_doc import doc_from_xml, WdNames


from model.logger import getTestLogger
_log = getTestLogger(__name__)

#==================================================================================================

WIKIPEDIA_NAMESPACE = 'http://www.mediawiki.org/xml/export-0.8/'

def make_wikipedia_tag(tag):
    '''Creates tag full name according to wikipedia namespace
    @param tag: string. Tag in wikipedia xml dump file, such as 'page'
    @return: tag with namespace: {WIKIPEDIA_NAMESPACE}{tag}"
    '''
    return "{%s}%s" % (WIKIPEDIA_NAMESPACE, tag)

# wikipedia page tag
PAGE_TAG = make_wikipedia_tag('page')

# parsed doc tag
DOC_TAG = 'doc'


def my_xfind(doc, xp):
    '''
    @return: tag in xp
    '''
    new_xp = xp.replace('/', '/{{{}}}'.format(WIKIPEDIA_NAMESPACE))
    return doc.find(new_xp)
    
def doc_from_wikipagexml(page_tag):
    tid    = my_xfind(page_tag,'./id').text
    title  = my_xfind(page_tag,'./title').text
    text   = my_xfind(page_tag,'./revision/text').text   
    rev_id = my_xfind(page_tag,'./revision/id').text         
    
    _log.info("Page proceeded: {}".format(title) )   
    wikidoc = WikiDocument(int(tid), title, text,int(rev_id))
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
    pages = iterate_xml(f, PAGE_TAG)
    return gen_apply(pages, doc_from_wikipagexml, clean_tarnform)

def iterate_wiki_pages(f):
    pages = iterate_xml(f, PAGE_TAG)
    return gen_apply(pages, doc_from_wikipagexml)

# load xml of parsed dumeb repr
def iterate_wiki_doc(f):
    docs = iterate_xml(f, DOC_TAG)
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
 
def parse_xml(filename): 
    if filename.endswith(".gzip"):
        filename = gzip.open(filename)
    return etree.parse(filename)

# for log purpurses
def _cut_text(text):
    ''' text will be cut to fit screen'''
    if text is None: return "!None"
    return text[:80] + "... total chars {}".format(len(text))


            
