'''
Created on Nov 28, 2012

@author: inesmeya
'''
import mwparserfromhell
import model.logger as _log
import WikiExtractor

class WikiTextProcessor(object):
    
    def __init__(self,text,normalize=False, collapse=True ):
        self.text = text
        self.wikicode = mwparserfromhell.parse(text)
        self.normalize = normalize
        self.collapse = collapse
        
    def get_strip_code(self):
        '''returns text includes links and sections'''
        _log.INFO("Retrive Clean text. ={}".format(self.normalize))
        clean_text = self.wikicode.strip_code(normalize=self.normalize, collapse=self.collapse)

        return clean_text
    
    def get_clean_text(self):
        '''returns text includes links and sections'''
        _log.INFO("Retrive Clean text. ={}".format(self.normalize))
        clean_text = self.wikicode.strip_code(normalize=self.normalize, collapse=self.collapse)

        return clean_text
            
    def get_text_only(self):
        '''returns only text nodes'''
        _log.INFO("Retrive text_only.") 
        text = "".join((n.value for n in self.wikicode.ifilter_text()))
        
        if self.collapse:
            while "\n\n" in text:
                text = text.replace("\n\n", "\n")
        return text
    
    
    def get_links(self):
        return self.wikicode.ifilter_links()