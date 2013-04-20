'''
Here are we save all peaces of code that we remove from project
'''
#TODO: Do we need this?
# def download_parser(subparsers):
#     # create the parser for the "download" command
#     parser_download = subparsers.add_parser('download', help='Downloads Wikipedia dump file from Wikipedia site')
#     parser_download.add_argument("-s", "--source", type=str, help='url of dump file path')
#     parser_download.add_argument("-o", "--output", type=str, help='output dump file path')
#     parser_download.set_defaults(func=handlers.download)
#     

#     def __repr__(self):
#         text = self.wiki_text
#         if text is None:
#             text = self.clean_text
#         if text != None:
#             text = (text)[:80]
#                   
#         retval = """
#             doc_id = {id} 
#             title = {title} 
#             wiki_text = {wiki_text} 
#             rev_id = {rev_id}""".format(
#                    id=self.id, 
#                    title=self.title,
#                    wiki_text=text, 
#                    rev_id=self.rev_id)
#         return retval 

#import bz2
#c = bz2.compress("wnload.add_argument(")


'''    
These methods can be deleted, the are here just as a reminder of old usage 

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
        
    
    def build(self, parsed_dump, builed_wdb, stemmer=None):
        ensure_dir(builed_wdb)
       
    def build_dbw(self, parsed_dump, stemmer=None):
        """ builds WikiRep database.
            @param parsed_dump: Wikipedia source xml (etc. wikiparsed.xml)
            @return: db wrapper
        """
        if not os.path.isfile(parsed_dump):
            raise Exception("File ")
                
        #TODO: add parsed page reader
        xml_pages = parse_tools.iterate_wiki_doc(parsed_dump)
        for doc in xml_pages:
            self.db_builder.add_document(doc)
        db = self.db_builder.build()
        return db

            

    
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
    

    def parse2(self,dump_reader, parsed_xml_writer):
        """ Parses wiki_dump.
            @param wiki_dump: input wikipedia dump filename  
            @param parsed_xml_path: output xml filename 
        """
        #INFO('Executing parse process on dump: {}'.format(wiki_dump_path))
        INFO('Output to Dump path: {}'.format(parsed_xml_path))
 
        #ensure_dir(parsed_xml_path)
 
        #open wikipedia dump according to format (compressed or not)       
        if wiki_dump_path.endswith('.bz2'):
            dump_file = bz2.BZ2File(wiki_dump_path, 'r')
        else:
            dump_file = open(wiki_dump_path, 'r')
        
        #open parsed wikipedia
        parsed_xml = codecs.open(parsed_xml_path, 'w',encoding="UTF-8") 
        
        #parse all pages
        parsed_xml.write('<?xml version="1.0" ?>\n')
        parsed_xml.write('<wikirep>\n')
        #for doc in gen_apply(iterate_wiki_pages(wik)
        parsed_xml.write('</wikirep>\n')
        
        #close files
        dump_file.close()
        parsed_xml.close()
        
        
    def parse(self, src_wiki_dump, output=None):
        """ Parses wiki_dump.
            @param wiki_dump: input wikipedia dump filename  
            @param output: output xml filename 
            @return: parsed xml pages
        """
        return parse_tools.extract_clean_pages(src_wiki_dump, keep_sections=False, keep_links=False)
''' 

def download_all(self, wiki_dump=None):
    """ Download whole wikipedia into dump file.
        @param src_url: url of dump file (if not specified default is used)
        @param wiki_dump: output dump filename, etc. wikidump.bz2 (if not specified default is used)
    """
    raise NotImplemented()

