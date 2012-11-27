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

    wiki_knowledge = getWikiKnowledge()    
    wiki_knowledge.build(args.src)      
    wiki_knowledge.save_to_disk(args.dst)
    
        
    
def parse(args):
    pass
def download(args):
    pass
def compare(args):
    pass
def get_value(args):
    pass
