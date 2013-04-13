#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Oct 15, 2012

@author: inesmeya
'''
from subprocess import Popen, PIPE
import gzip
import urllib2 

import logging
import model.logger as lg
_log = lg.getLogger(__name__)  #lg.mainlog # logging.getLogger("webtools")#__name__)

import os
def ensure_dir(f):
    d = os.path.dirname(f)
    if len(d)== 0:
        return
    if not os.path.exists(d):
        os.makedirs(d)

base_xml_url = "http://en.wikipedia.org/wiki/Special:Export/"

def get_article_xml_url(article_title):
    url = base_xml_url + article_title
    return url

def get_wiki_xmlpage_wget(article_title):
    url = get_article_xml_url(article_title)
    try:
        cmd = ["wget", '-qO-', '-S', url]
        p = Popen(cmd, stdout=PIPE, stderr=PIPE)
    except:
        "retry on macOS"
        cmd = ["/usr/local/bin/wget", '-qO-', '-S', url]
        p = Popen(cmd, stdout=PIPE, stderr=PIPE)
        
    output, errors = p.communicate()
    if p.returncode:
        raise Exception(errors)
    else:
        return str(output) # Print stdout from cmd call

def get_wiki_xmlpage_urllib(url):
    ''' note on using urllib 
    [http://meta.wikimedia.org/wiki/Bot_policy#Unacceptable_usage]
    Wikipedia's stance is:
        Data retrieval: Bots may not be used to retrieve bulk content
        for any use not directly related to an approved bot task.
        This includes dynamically loading pages from another website,
        which may result in the website being blacklisted and permanently denied access.
        If you would like to download bulk content or mirror a project, 
        please do so by download or hosting your own copy of our database.

    That is why Python is blocked. You're supposed to download data dumps.
    
    source code of solution from:
        http://stackoverflow.com/questions/3336549/pythons-urllib2-why-do-i-get-error-403-when-i-urlopen-a-wikipedia-page

    '''
    req = urllib2.Request(url, headers={'User-Agent' : "Wikip Browsers"})     
    
    file_handler = urllib2.urlopen(req)
    xml_text = file_handler.read()
    file_handler.close()
    return xml_text

def get_wiki_xmlpage(url):
    try:
        _log.debug("Try using get_wiki_xmlpage_urllib:{}".format(url))
        return get_wiki_xmlpage_urllib(url)
    except Exception as e:
        _log.warning("Failed to get wiki page using urllib.\n Reason: {}".format(e))
        _log.warning("trying using wget")
        
        return get_wiki_xmlpage_wget(url)

def get_article_xmlpage(artice_title):
    url = get_article_xml_url(artice_title)
    return get_wiki_xmlpage(url)

def make_articles_dump(titles, outstream):
    first=True    
    for title in titles:
        xml = get_article_xmlpage(title)
        if first:
            end = xml.find('</mediawiki>')
            outstream.write(xml[:end])
            first=False
        else:
            start = xml.find('<page>')
            end   = xml.find('</page>') + len('</page>')
            outstream.write(xml[start:end])
    outstream.write('\n</mediawiki>\n')

_NS = 'http://www.mediawiki.org/xml/export-0.8/'

def mk_tag(tag):
    return "{%s}%s" % (_NS, tag)


def articles_dump_to_file(titles, filename, compress=False, compresslevel=9):
    """
    The compresslevel argument is an integer from 1 to 9 controlling the
    level of compression; 1 is fastest and produces the least compression,
    and 9 is slowest and produces the most compression.  The default here is 9.
    """
    
    ensure_dir(filename)
    if compress: 
        dump = gzip.open(filename + ".gzip", 'w', compresslevel=compresslevel) 
    else:
        dump = open(filename ,'w')
    make_articles_dump(titles, dump)
    dump.flush()
    dump.close()

if __name__ == '__main__':
    pass
