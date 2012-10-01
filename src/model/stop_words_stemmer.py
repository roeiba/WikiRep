'''
Created on Sep 27, 2012

@author: inesmeya
'''
from simple_splitter import SimpleSplitter

default_stop_words_list = stop_words = [ 'i', 'in', 'a', 'to', 'the', 'it', 'have', 'haven\'t', 'was', 'but', 'is', 'be', 'from' ]




class StopWordsStemmer(object):
    '''
    filters words
    '''
    def __init__(self,stop_words_list=None):
        '''
        @param stop_words_list: list of words to drop
        '''
        self.stop_words_list = stop_words_list or []                                    
        self.splitter = SimpleSplitter()
            
    def process_text(self,raw_text):
        ''' @param raw_text: string
            @return: list of words, 
        
        '''
        raw_words = self.splitter.split(raw_text)
        stemed_words = []
        for word in  raw_words:
            stemed_word = self.process_word(word)
            if stemed_word:
                stemed_words.append(word)
        return stemed_words
        
    def process_word(self,word):
        """ @return: None if word in stop_word_list, otherwise word itself
        """
        return None if word in self.stop_words_list else word
    
        