#!/usr/bin/env python2.7

import sys
import logging
from argparse import ArgumentParser
from model.logger import mainlog as _log
from wiki_knows import wiki_knowledge
from model.utilits import get_top 

# ------------------- Default configuration ----------------------------------------
class DConfig:
    dump_path = "data_output/wikidump.xml"
    parsed_path ="data_output/wikiparsed.xml"
    wdb_path = "data_output/wikibuild.wdb"
                  
class colors(object):
    BLUE = '\x1b[34m'
    RESET = '\x1b[39m'
    YELLOW = '\x1b[33m'
    GREEN = '\x1b[32m'
    WHITE = '\x1b[37m'
    CYAN = '\x1b[36m'
    BLACK = '\x1b[30m'
    MAGENTA = '\x1b[35m'
    RED = '\x1b[31m'
    
#####################################################################################
# Parser methods: Each method is name action_parser
#####################################################################################

def makedump_parser(subparsers):
    # create the parser for the "make" command
    parser_makedump = subparsers.add_parser('makedump',
         help="""Download specified articles from wikipedia site, 
                 merges them into one file and compress it as wikipedia dump file""")
    parser_makedump.add_argument("article", nargs="+", help="List of articles for download" )
    parser_makedump.add_argument("-dump", help="output file name", dest="dumpfile", default=DConfig.dump_path)
    
    def makedump(args):
        _log.debug("run makedump with args={}".format(args))
        wiki_knowledge.make_dump(args.dumpfile, args.article)
    
    parser_makedump.set_defaults(func=makedump)


def parse_parser(subparsers):
    # create the parser for the "parse" command
    parser_parse = subparsers.add_parser('parse', 
        help="""Parses dump file into WikiDocuments in XML representation - Each of which contains:
        doc_id: Wikipedia concept's ID
        title: Wikipedia concept's title
        text: - Clean text 
        rev_id: - Wikipedia concept's revision""")
    parser_parse.add_argument("-d", "--dump",   help='input dump file path', default=DConfig.dump_path)
    parser_parse.add_argument("-o", "--output", help='output XML file path',default=DConfig.parsed_path)
    
    def parse(args):
        _log.debug("run parse with args={}".format(args))
        wiki_knowledge.parse_dump(args.dump, args.output)
    
    parser_parse.set_defaults(func=parse)

def build_parser(subparsers):
    # create the parser for the "build" command
    parser_build = subparsers.add_parser('build', 
        help="Iterates all WikiDocuments found in src and builds a words database (DatabaseWrapper) and saves it to dst")
    parser_build.add_argument("--src", type=str, help='input parsed file path', default=DConfig.parsed_path)
    parser_build.add_argument("--dst", type=str, help='output wdb filename',default=DConfig.wdb_path)
    
    def build(args):
        _log.debug("run build with args={}".format(args))
        wiki_knowledge.build_database_wrapper_to_file(args.src, args.dst)
        
    parser_build.set_defaults(func=build)
    
def compare_parser(subparsers):
    # create the parser for the "compare" command
    parser_compare = subparsers.add_parser('compare', 
        help="Compares two texts according to words database at 'wikibuild.wdb'")
    parser_compare.add_argument("--dbpath", type=str, nargs=1, default=DConfig.wdb_path,
        help='word database path')
    parser_compare.add_argument("--text1", type=str, help='first text')
    parser_compare.add_argument("--text2", type=str,  help='second text')
    
    def compare(args):
        _log.debug("run build with args={}".format(args))
        correlation = wiki_knowledge.compare(args.dbpath, args.text1, args.text2)
        _log.info("correlation = {0}".format(correlation))
    
    parser_compare.set_defaults(func=compare)
    
def get_value_parser(subparsers):
    # create the parser for the "get_value" command
    parser_get_value = subparsers.add_parser('get_value', 
        help="Calculates the text vector in Wikipedia concepts space according to workds database at 'wikibuild.wdb'")
    parser_get_value.add_argument("--dbpath", type=str, nargs=1, default=DConfig.wdb_path,
        help='word database path')
    parser_get_value.add_argument("text", type=str, help='text for value calculation')
    
    def get_value(args):
        _log.debug("run build with args={}".format(args))
        if isinstance(args.dbpath , list):
            args.dbpath=args.dbpath[0]
        wdb = wiki_knowledge.load_db_wrapper_from_wdb(args.dbpath)
        v = wdb.get_text_centroid(args.text)
        
        _log.info("vector = {0}".format(v.data))
            
    parser_get_value.set_defaults(func=get_value) 


def get_top_topics_parser(subparsers):
    # create the parser for the "get_value" command
    p = subparsers.add_parser('get_top_topics', 
        help="at 'wikibuild.wdb'")
    p.add_argument("--dbpath", type=str, nargs=1, default=DConfig.wdb_path,
        help='word database path')
    p.add_argument("--text_path", type=str, help='file with text for value calculation')
    
    def get_top_topics(args):
        _log.debug("run build with args={}".format(args))
        if isinstance(args.dbpath , list):
            args.dbpath=args.dbpath[0]
        if isinstance(args.text_path , list):
            args.text_path=args.text_path[0]
        d = wiki_knowledge.get_value_from_file(args.dbpath, args.text_path)
        top = get_top(d,5)
        print "closests topics:"
        for t,v in top:
            print "{}:{:2.4f}".format(t,v)
        
    p.set_defaults(func=get_top_topics) 
        
# ------------------------------ Top Level Parser -------------------------------------------------
def create_argument_parser():
    # from argparse import ArgumentParser
    # create the top-level parser
    parser = ArgumentParser(prog='WikiRep', description='wikipedia dump creator. ')
    parser.add_argument('-v', action='append_const', const=1, dest='verbose', default=[])
    parser.add_argument("--logs", action='store_true', default=False,
                        help="Save logs. Stores logs on local server")
    # create sub parsers
    subparsers = parser.add_subparsers(help='sub-command help', title='Sub-commands', 
                        description='The valid commands are:')
    makedump_parser(subparsers)
    #download_parser(subparsers)
    parse_parser(subparsers)
    build_parser(subparsers)
    compare_parser(subparsers)
    get_value_parser(subparsers)
    get_top_topics_parser(subparsers)
    return parser

# ------------------------------ AUX -------------------------------------------------
def _error(msg):
    print("{}\n{}\n{}\n".format(colors.RED, msg, colors.RESET))
  
def print_failure_info():
    _error("\n")
    _error("-"*80)
    _error("wikiknow execution failed!")
    _error('Additional information can be at our site: https://github.com/roeiba/WikiRep/wiki')

def _configure_logging(args):
    verbosity_level = len(args.verbose)
    if verbosity_level == 0:
        level = logging.WARNING
    elif verbosity_level == 1:
        level = logging.INFO
    else:
        level = logging.DEBUG
    logging.basicConfig(level=level)
    
# ------------------------------ MAIN: Entry Point -------------------------------------------------        
def main(argv=None):
    try:
        print "Starting..."
        if argv is None:
            argv = sys.argv[1:]
        parser = create_argument_parser()
        args = parser.parse_args()
        _configure_logging(args)
        args.func(args)
        print "Finished."        
    
    except SystemExit, e:
        return e.code
    except:
        import traceback
        traceback.print_exc()
        print_failure_info()
        return 2
    return 0
    
if __name__ == "__main__":
    sys.exit(main())
