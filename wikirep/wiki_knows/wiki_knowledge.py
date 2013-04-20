#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import bz2
from model.db_builder import DbBuilder
from model import stemmers
from model.wiki_doc import wiki_doc_to_xml
from model.semantic_interpreter import SemanticComparer

from parsers import web_tools
from parsers import parse_tools
import codecs

from model.logger import getLogger
_log = getLogger("WikiKnows")

import os
import pickle
from model.database_wrapper import DatabaseWrapper, DbContant
def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)

def make_dump(wiki_dump, articles_titles, compress=False):
    """ Download specified articles from Wikipedia site, 
        merges them into one file, compresses it as Wikipedia dump file
        @param articles_titles: article's canonic name on Wikipedia web page
        @param wiki_dump: output filename (if not specified default is used)
    """
    _log.debug("-"*80)
    _log.info('Executing makedump process on articles: {}'.format(articles_titles))
    _log.info('Dump path: {}'.format(wiki_dump))
      
    web_tools.articles_dump_to_file(articles_titles, wiki_dump, compress)
    
def _parse_dump(dump_reader,parsed_xml_writer):
    """ Parses wiki_dump.    
        @param dump_reader: file-like stream with wikipedia dump open
        @param output: output xml filename 
        @return: parsed xml pages
    """ 
    docs = parse_tools.iterate_clean_pages(dump_reader, parse_tools.cleaner_WikiTextProcessor)
    
    doc_number = 0
    for doc in docs:
        doc_number+=1 
        _log.info("Done parsing document #{}:{}".format(doc_number, doc.title))
        
        doc_tag = wiki_doc_to_xml(doc)
        parsed_xml_writer.write(doc_tag)

    _log.info("Finish parsing. Total documents: #{}".format(doc_number))
                                                    
        
def parse_dump(wiki_dump_path, parsed_xml_path):
    """ Parses wiki_dump.
    @param wiki_dump: input wikipedia dump filename  
            @param parsed_xml_path: output xml filename 
    """
    _log.debug("-"*80)
    _log.info('Executing parse process on dump: {}'.format(wiki_dump_path))
    _log.info('Output to Dump path: {}'.format(parsed_xml_path))
   
    ensure_dir(parsed_xml_path)
    
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
    
    _parse_dump(dump_file, parsed_xml)
                                                     
    #self._parse_dump(dump_file,parsed_xml)
    parsed_xml.write('</wikirep>\n')
    
    #close files
    dump_file.close()
    parsed_xml.close()

def compare(path, text1, text2):
    wdb = load_db_wrapper_from_wdb(path)
    comparer = SemanticComparer(wdb)
    corelation = comparer.compare(text1, text2)
    return corelation
                        
def load_db_wrapper_from_wdb(path):
    """ 
    loads Database from pickle file DbContant object
    @param path: path to pickle file DbContant object
    @return: DatabaseWrapper
    """
    
    with open(path, 'rb') as infile:
        db_content = pickle.load(infile)
    stemmer = stemmers.get_stemmer_by_name(db_content.stemmer_name)
    db_wrapper = DatabaseWrapper(
                   db_content.weight_matrix,
                   db_content.concepts_index,
                   db_content.words_index,
                   stemmer )    
    return db_wrapper
    
def save_db_wrapper_to_wdb(db_wrapper, path):
    """ Saves provided dw_wrapper to path wdb file"
    @param dw_wrapper: DatabaseWrapper to save
    @note: loading is by load_db_wrapper_from_wdb. Stemmer saved by name, and then loaded by load function
    """
    ensure_dir(path)
    db_content = DbContant(
                   db_wrapper.wieght_matrix,
                   db_wrapper.concepts_index,
                   db_wrapper.words_index,
                   db_wrapper.stemmer.get_name() )
    with open(path, 'wb') as outfile:
        pickle.dump(db_content, outfile, pickle.HIGHEST_PROTOCOL)
        
###################################################################################
# methods for building database, with two main usages:
# 1. Build an instance of db_wrapper for testing and simple executions
# 2. Build a real database based on a wiki dump, for production usages 
###################################################################################
def build_database_wrapper(parsed_dump, stemmer=None):
    """ builds WikiRep database.
        @param parsed_dump: Wikipedia parced xml (etc. wikiparsed.xml)
        @return: db wrapper
    """
    _log.debug("-"*80)
    _log.info("Building DB from parsed dump:{0}".format(parsed_dump))
    
    if stemmer is None: stemmer = stemmers.StopWordsStemmer()
    db_builder = DbBuilder(stemmer)
    if not os.path.isfile(parsed_dump):
        raise Exception("Parsed dump doesnt exists: File {0}".format(parsed_dump))
            
    #TODO: add parsed page reader
    xml_pages = parse_tools.iterate_wiki_doc(parsed_dump)
    doc_count = 0
    for doc in xml_pages:
        doc_count+=1
        _log.debug("Adding document #{0}:{0}".format(doc_count, doc.title))
        db_builder.add_document(doc)
    db = db_builder.build()
    _log.info("Database was created with #{0} documents".format(doc_count))
    return db
    
def build_database_wrapper_to_file(parsed_dump, build_wdb_path, stemmer=None):
    """ builds WikiRep database and save it to pickle file
        @param parsed_dump: Wikipedia parced xml (etc. wikiparsed.xml)
        @return: db wrapper
    """
    db_wrapper = build_database_wrapper(parsed_dump, stemmer)
    ensure_dir(build_wdb_path)
    _log.info("Saving to file: {0}".format(build_wdb_path))
    save_db_wrapper_to_wdb(db_wrapper, build_wdb_path)



        
