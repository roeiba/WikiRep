#!/usr/bin/env python2.7
from model.wiki_knowledge import WikiKnowledge
import sys
    
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
    
    
def create_argument_parser():
    from argparse import ArgumentParser

    parser = ArgumentParser(description='wikipedia dump creator. ')
    parser.add_argument("--articles", nargs="*", default=['Knowledge'],
                        help="Download specified articles from wikipedia site," + 
                        "merges them into one file and compress it as wikipedia dump file " )
    
    parser.add_argument("--logs", action='store_true', default=False,
                        help="Save logs. Stores logs on local server")
        
    return parser

def _error(msg):
    print("{}{}{}".format(colors.RED, msg, colors.RESET))
    
def print_failure_info():
    _error("\n")
    _error("-"*80)
    _error("wikiknow execution failed!")
    _error('Additional information can be at our site: https://github.com/roeiba/WikiRep/wiki')
    
def main(argv=None):
    try:
        print "Starting..."
        if argv is None:
            argv = sys.argv[1:]
        parser = create_argument_parser()
        args = parser.parse_args()
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
