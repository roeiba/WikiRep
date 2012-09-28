'''
Created on Sep 28, 2012

@author: inesmeya
'''
from concept import Concept 

class DbBuilder(object):
    '''
    classdocs
    '''


    def __init__(self,stemmer):
        '''
        Constructor
        '''
        self._last_id = -1
        self.stemmer = stemmer
        self.concepts_list = []

    def _generate_concept_id(self):
        ''' @return: sequential id's for concepts '''
        self._last_id+=1
        return self._last_id
        
    def add_document(self,doc):
        """ Converts document to concept 
            @param doc: sould have title and raw_text
        """
        cid = self._generate_concept_id()
        word_list = self.stemmer.process_text(doc.raw_text)
        new_concept = Concept(cid, doc.title, word_list)
        self.concepts_list.append(new_concept)
         
    def build(self):
        pass
        
        
        
                