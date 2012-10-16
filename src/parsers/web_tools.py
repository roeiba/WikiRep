'''
Created on Oct 15, 2012

@author: inesmeya
'''
from subprocess import Popen, PIPE
import urllib2 

base_xml_url = "http://en.wikipedia.org/wiki/Special:Export/"

def get_article_xml_url(article_title):
    url = base_xml_url + article_title
    return url

def get_wiki_xmlpage_wget(article_title):
    url = get_article_xml_url(article_title)
    cmd = ["/usr/local/bin/wget", '-qO-', '-S', url]
    p = Popen(cmd, stdout=PIPE, stderr=PIPE)
    output, errors = p.communicate()
    if p.returncode:
        raise Exception(errors)
    else:
        return str(output) # Print stdout from cmd call

def get_wiki_xmlpage_urllib(article_title):
    ''' note on using urllib 
    [http://meta.wikimedia.org/wiki/Bot_policy#Unacceptable_usage]
    Wikipedias stance is:
        Data retrieval: Bots may not be used to retrieve bulk content
        for any use not directly related to an approved bot task.
        This includes dynamically loading pages from another website,
        which may result in the website being blacklisted and permanently denied access.
        If you would like to download bulk content or mirror a project, 
        please do so by downloading or hosting your own copy of our database.

    That is why Python is blocked. You're supposed to download data dumps.
    
    source code of solution from:
        http://stackoverflow.com/questions/3336549/pythons-urllib2-why-do-i-get-error-403-when-i-urlopen-a-wikipedia-page

    '''
    url = get_article_xml_url(article_title)
    req = urllib2.Request(url, headers={'User-Agent' : "Wikip Browser"})     
    
    file_handler = urllib2.urlopen(req)
    xml_text = file_handler.read()
    file_handler.close()
    return xml_text

def get_wiki_xmlpage(article_title):
    try:
        return get_wiki_xmlpage_urllib(article_title)
    except:
        return get_wiki_xmlpage_wget(article_title)
        

def make_articles_dump(titles, outstream):
    first=True    
    for title in titles:
        xml = get_wiki_xmlpage(title)
        if first:
            end = xml.find('</mediawiki>')
            outstream.write(xml[:end])
            first=False
        else:
            start = xml.find('<page>')
            end   = xml.find('</page>') + len('</page>')
            outstream.write(xml[start:end])
    outstream.write('\n</mediawiki>\n')

_NS = 'http://www.mediawiki.org/xml/export-0.7/'
def mk_tag(tag):
    return "{%s}%s" % (_NS, tag)


def articles_dump_to_file(titles, filename):
    dump = open(filename,'w')
    make_articles_dump(titles,dump)
    dump.flush()
    dump.close()

if __name__ == '__main__':
    pass