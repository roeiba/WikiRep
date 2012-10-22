
class WikiDocument(object):
    def __init__(self, doc_id, title, raw_text, rev_id=None):
        self.id = doc_id
        self.title = title
        self.raw_text = raw_text 
        self.rev_id = rev_id
    