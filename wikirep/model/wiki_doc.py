from model.logger import *

class WdNames:
    CLEAN_TEXT = 'clean_text'
    LINKS = 'links'
 

class WikiDocument(object):
    def __init__(self, doc_id, title, raw_text, rev_id=None):
        self.id = doc_id
        self.title = title
        self.raw_text = raw_text 
        self.rev_id = rev_id
        self.meta = {}
        DEBUG("Created WikiDocument: {}".format(self))
    
    def __repr__(self):
        retval = """
            doc_id = {id} 
            title = {title} 
            raw_text = {raw_text} 
            rev_id = {rev_id}""".format(
                   id=self.id, 
                   title=self.title,
                   raw_text=log_text(self.raw_text), 
                   rev_id=self.rev_id)
        return retval 
    
    def to_xml(self):
        smxl = """
< doc id="{}" title="{}" rev_id="{}"> 
       {} 
</doc>
""".format(self.id, self.title, self.rev_id, self.raw_text)
        return smxl
        
        
        
        
        