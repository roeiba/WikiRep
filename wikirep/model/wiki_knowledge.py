from model.db_builder import DbBuilder
from model import stop_words_stemmer
from model.wiki_doc import WikiDocument
from model.semantic_interpreter import SemanticInterpreter
from model import math_utils
from parsers import web_tools
from parsers import parse_tools
from logger import *


class WikiKnowledge(object):
    """
        Example
        --------
        >>> wiki_knowledge = WikiKnowledge()
        
        >>> wiki_knowledge.make_dump(dump_file, *articles, compress=False)            
                create dump from articles list (if a dump already exist, this step may be skipped)
        
        >>> wiki_knowledge.build(dump_file, None)
                builds SemanticIntepreter according to dump file
                
        >>> wiki_knowledge.compare(text1, text2)
                Compares two texts in wikipedia space.

        >>> wiki_knowledge.get_text_value(text)
                returns the text vector in wikipedia space. 
    """
    def __init__(self, 
                 stemmer=None, 
                 compare_method=None):
        self.stemmer = stemmer
        self.default_compare = compare_method
        self.init()

    def init(self):
        if self.default_compare is None: self.default_compare = math_utils.cosine_metrics
        if self.stemmer is None: self.stemmer = stop_words_stemmer.get_default_stemmer()
        self.semantic_intepreter = None
        self.db_builder = DbBuilder(self.stemmer)
        
    def make_dump(self, wiki_dump, *articles_titles, **kwargs):
        """ Download specified articles from Wikipedia site, 
            merges them into one file, compresses it as Wikipedia dump file
            @param articles_titles: article's canonic name on Wikipedia web page
            @param wiki_dump: output filename (if not specified default is used)
        """
        web_tools.articles_dump_to_file(articles_titles, wiki_dump, **kwargs)
    
    def download_all(self, wiki_dump=None):
        """ Download whole wikipedia into dump file.
            @param src_url: url of dump file (if not specified default is used)
            @param wiki_dump: output dump filename, etc. wikidump.bz2 (if not specified default is used)
        """
        raise NotImplemented()
    
    def parse(self, src_wiki_dump, output=None):
        """ Parses wiki_dump.
            @param wiki_dump: input wikipedia dump filename  
            @param output: output xml filename 
            @return: parsed xml pages
        """
        return parse_tools.extract_clean_pages(src_wiki_dump, keep_sections=False, keep_links=False)
        
    def build(self, src, stemmer=None):
        """ builds WikiRep database.
            @param src: Wikipedia source xml (etc. wikiparsed.xml)
        """
        
        xml_pages = self.parse(src)
        for doc_id, title, text, rev_id in xml_pages:
            doc = WikiDocument(doc_id=doc_id, title=title, raw_text=text, rev_id=rev_id)
            self.db_builder.add_document(doc)
        self._build_semantic_interpreter()

            
    def compare(self, text1, text2, compare_method=None):
        """
            Compares two texts in wikipedia space.
            @param db: WikiRep database filename
        """
        #semantic_interpreter = SemanticInterpreter(database)
        #generate weighted vectors
        msg_format = "Text: {text}\nWieght vector: {vector}"
        
        w_vector_1 = self.get_text_value(text1)
        DEBUG( msg_format.format(text=text1, vector=w_vector_1) )
        
        w_vector_2 = self.get_text_value(text2)
        DEBUG( msg_format.format(text=text2, vector=w_vector_2) )
        
        #compare vectors
        if compare_method is None: compare_method = self.default_compare
        correlation = compare_method(w_vector_1, w_vector_2)
        DEBUG( "correlation is: {}".format(correlation) )
        return correlation
        
    def get_text_value(self, text):
        """
            returns the text vector in wikipedia space.
        """
        if self.semantic_intepreter is None:
            raise Exception("Semantic interpreter is not initialized! Make sure to use build().")
        retval = self.semantic_intepreter.build_weighted_vector(text)
        DEBUG("text vector: {}".format(retval))
        return retval
    
    def save_to_disk(self, output):
        """
            Saves the SemanticInterpreter database to disk
            @param output: WikiRep database output file
        """
        self.db_builder.save(output)
    
    def load_from_disk(self, src):
        self.init()
        self.db_builder.load_concepts(src)
        self._build_semantic_interpreter()
    
    def analize(self, text1, db):
        """
            #TODO: Define method and implement
            @param db: WikiRep database filename
        """
        pass
    
    def _build_semantic_interpreter(self):
        db = self.db_builder.build()
        self.semantic_intepreter = SemanticInterpreter(db, self.stemmer)
        
#==========================================================================================

_defaultWikiKnowledge = WikiKnowledge()

def getWikiKnowledge():
    return _defaultWikiKnowledge
    

        