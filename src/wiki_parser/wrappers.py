'''
Created on Oct 1, 2012

@author: roeib
'''
import runpy
from subprocess import *
import WikiExtractor 
# ===================  wiki ===============================

def get_wiki_page(article_title):
    link = "http://en.wikipedia.org/wiki/Special:Export/" + article_title
    cmd = ["/usr/local/bin/wget", '-qO-', '-S', link]
    p = Popen(cmd, stdout=PIPE, stderr=PIPE)
    output, errors = p.communicate()
    if p.returncode:
        raise Exception(errors)
    else:
        # Print stdout from cmd call
        return str(output)

def get_wiki_page_clean(article_title):
    xml_str = get_wiki_page(article_title)
    clean_str =  WikiExtractor.run(xml_str,keep_sections=False,keep_links=True)
    return clean_str 


if __name__ == "__main__":
    print get_wiki_page_clean("Knowledge")