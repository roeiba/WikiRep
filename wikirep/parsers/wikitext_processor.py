'''
Created on Nov 28, 2012

@author: inesmeya
'''
import mwparserfromhell

class WikiTextProcessor(object):
    
    def __init__(self,text,normalize=False, collapse=True ):
        self.wikicode = mwparserfromhell.parse(text)
        self.normalize = normalize
        self.collapse = collapse
        
    def get_clean_text(self):
        '''returns text includes links and sections'''
        clean_text = self.wikicode.strip_code(self.normalize, self.collapse)
        return clean_text
        
    def get_text_only(self):
        '''returns only text nodes'''
        nodes = self.wikicode.ifilter_text()
        if self.collapse:
            stripped = "".join(nodes).strip("\n")
            while "\n\n\n" in stripped:
                stripped = stripped.replace("\n\n\n", "\n\n")
            return stripped
        else:
            return "".join(nodes)
    
    def get_links(self):
        return self.wikicode.ifilter_links()