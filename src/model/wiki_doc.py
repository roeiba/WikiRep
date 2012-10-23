from model.logger import *

class WikiDocument(object):
    def __init__(self, doc_id, title, raw_text, rev_id=None):
        self.id = doc_id
        self.title = title
        self.raw_text = raw_text 
        self.rev_id = rev_id
        DEBUG("Created WikiDocument: {}".format(self))
    
    def __str__(self):
        retval = """
            doc_id = {id} 
            title = {title} 
            raw_text = {raw_text}... 
            rev_id = {rev_id}""".format(
                   id=self.id, 
                   title=self.title,
                   raw_text=self.raw_text[:70], 
                   rev_id=self.rev_id)
        return retval 
    