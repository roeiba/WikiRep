'''
Created on Sep 28, 2012

@author: inesmeya
'''

from collections import Counter, OrderedDict
from math_utils import count_to_tf

class OrderedCounter(Counter, OrderedDict):
    '''Counter that remembers the order elements are first encountered'''

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)
    

class Concept(object):
    '''
    Represents a document as bag of words. 

    Related Article
        Name: Wikipedia-based Semantic Interpretation for Natural Language Processing
        Short name: 2009_full
    '''
    def __init__(self, concept_id, title, word_list, revision_id=None):
        '''
        Creates object, calculates words occurrences 
        
        @param id: id of the concept (preferred the real Wikipedia ID)
        @param title: documents unique title
        @param word_list: list of words after stemming
        '''
        self.id = concept_id
        self.title = title
        self.revision_id = revision_id
        self._words_occurenece = OrderedCounter()
        for word in word_list:
            self._words_occurenece[word]+=1
        
    def get_word_ocurences(self,word):
        """number of times the word appears in the document"""
        return self._words_occurenece[word]
    
    def get_tf(self,word):
        "returns tf as described in 2009_full article at page 6"
        wc = self.get_word_ocurences(word)
        tf = count_to_tf(wc)
        return tf
    
    def get_all_words(self):
        """ @return: set of all words
        """
        return self._words_occurenece.keys()
    
    def interate_words(self):
        return self._words_occurenece.iterkeys()
    
    def get_words_dict(self):
        return self._words_occurenece
    