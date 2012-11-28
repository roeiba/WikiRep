#!/usr/bin/python
# -*- coding: utf-8 -*-
from model.logger import *
from model.wiki_knowledge import getWikiKnowledge


def makedump(args):
    DEBUG("run makedump with args={}".format(args))

    wiki_knowledge = getWikiKnowledge()
    wiki_knowledge.make_dump(args.dumpfile, *args.article)


def build(args):
    DEBUG("run with args={}".format(args))
    INFO('Executing makedump process on articles: {}'.format(args.article))
    INFO('Dump path: {}'.format(args.dumpfile))

    
def parse(args):
    DEBUG("run with args={}".format(args))

    
    wiki_knowledge = getWikiKnowledge()
    wiki_knowledge.parse_dump(args.dump, args.output)

    
    
def download(args):
    pass
def compare(args):
    pass
def get_value(args):
    pass
