'''
Created on Sep 19, 2012
'''

import concept_db
class ConceptsDbStub(concept_db.ConceptsDb):
    
    def __init__(self):
        self.concepts = ["concept1","concept2"]
        self.db = {
            'word1' : [ 0.5, 0.0],
            'word2' : [ 0.3, 0.7]
        }
        
    def get_concept_vector(self,word):
        """returns word's weigted vector
        """
        return self.db[word]
    
    def get_concept_index(self,concept):
        """Returns index of specified concept
        """
        return self.concepts.index(concept)
        
        