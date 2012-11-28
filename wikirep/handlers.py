from model.logger import *
from model.wiki_knowledge import getWikiKnowledge


def makedump(args):
    DEBUG("run with args={}".format(args))
    INFO('Executing makedump process on articles: {}'.format(args.article))
    INFO('Dump path: {}'.format(args.dumpfile))
    
    wiki_knowledge = getWikiKnowledge()
    wiki_knowledge.make_dump(args.dumpfile, *args.article)


def build(args):
    DEBUG("run with args={}".format(args))
    INFO('Executing makedump process on articles: {}'.format(args.article))
    INFO('Dump path: {}'.format(args.dumpfile))

    
def parse(args):
    DEBUG("run with args={}".format(args))
    INFO('Executing parse process on dump: {}'.format(args.dump))
    INFO('Output to Dump path: {}'.format(args.output))
    
    wiki_knowledge = getWikiKnowledge()
    pages = wiki_knowledge.parse(args.dump, args.output)
    for p in pages:
        print p
    
    
def download(args):
    pass
def compare(args):
    pass
def get_value(args):
    pass
