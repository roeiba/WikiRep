'''
Created on Sep 27, 2012

@author: inesmeya
'''
import re

default_stop_words_list = stop_words = [ 'i', 'in', 'a', 'to', 'the', 'it', 'have', 'haven\'t', 'was', 'but', 'is', 'be', 'from' ]


class SimpleSplitter(object):
    """ Should be use to splite string into list of words
        Currently used regular expression: "[a-z\-']+"
    """    
    def __init__(self):
        self.template =  re.compile ( "[a-z\-']+", re.I )

    def split(self,text):
        """ splits string text int list of words
            @param text: string
            @return: list of words 
        """
        return self.template.findall(text)


class StopWordsSteemer(object):
    '''
    filters words
    '''
    def __init__(self,stop_words_list=None):
        '''
        @param stop_words_list: list of words to drop
        '''
        self.stop_words_list = stop_words_list if stop_words_list else default_stop_words_list
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
                stemed_words.append(object)
        return stemed_words
        
    def process_word(self,word):
        """ @return: None if word in stop_word_list, otherwise word itself
        """
        return word if word in self.stop_words_list else None
    
        