'''
Created on Sep 28, 2012

@author: inesmeya
'''

from collections import Counter
from math import log10

class Concept(object):
    '''
    Contains info of processed document
    Related Article
        Name: Wikipedia-based Semantic Interpretation for Natural Language Processing
        Short name: 2009_full
    '''
    def __init__(self, cid, title, word_list):
        '''
        Creates object, calculates words occurences 
        
        @param cid: id of the concept
        @param title: documents unique title
        @param word_list: list of words after steamming
        '''
        self.id = cid
        self.title = title
        self._words_occurenece = Counter(word_list)
        
    def get_word_ocurences(self,word):
        """number of times the word appears in the document"""
        return self._words_occurenece[word]
    
    def get_tf(self,word):
        "returns tf as described in 2009_full article at page 6"
        wc = self.get_word_ocurences(word)
        tf = 1 + log10(wc) if wc > 0 else 0
        return tf
    
    def get_all_words(self):
        """ @return: set of all words
        """
        return set(self._words_occurenece.keys())

    