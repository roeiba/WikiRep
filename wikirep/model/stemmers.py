'''
Created on Sep 27, 2012

@author: inesmeya
'''
from simple_splitter import SimpleSplitter
from refs.porter import PorterStemmer as RefPorterStemmer

default_stop_words_list = stop_words = [ 
    'i', 'in', 'a', 'to', 'the', 'it', 'have', 'haven\'t', 'was', 'but', 'is',
    'be', 'from','even', 'on', 'and', 'for', 'less', 'always', 'that', 'some',
    'up', 'with', 'as', 'out', 'an', 'their', 'only', 'most', 'of', 'time', 'while',
    'because', 'end', 'since', 'get', 'you', 'has', 'its', 'will',  's', 'are'
]




def get_default_stemmer():
    return ComplexStemmer(LowerStemmer(), StopWordsStemmer(default_stop_words_list), PorterStemmer())

class BaseStemmer(object):
    
    splitter = SimpleSplitter()
        
    def process_text(self,clean_text):
        ''' @param clean_text: string
            @return: list of words, 
        
        '''
        raw_words = self.splitter.split(clean_text)
        stemed_words = []
        for word in  raw_words:
            stemed_word = self.process_word(word)
            if stemed_word:
                stemed_words.append(word)
        return stemed_words
    
    def process_word(self,word):
        raise NotImplementedError("this is base class: BaseStemmer")
    def get_name(self):
        return self.__class__    
    
class StopWordsStemmer(BaseStemmer):
    '''
    filters words
    '''
    def __init__(self,stop_words_list=None):
        '''
        @param stop_words_list: list of words to drop
        '''
        self.stop_words_list = default_stop_words_list if stop_words_list is None else stop_words_list                                    
        
    def process_word(self, word):
        """ @return: None if word in stop_word_list, otherwise word itself
        """
        return None if word in self.stop_words_list else word
    

class PorterStemmer(BaseStemmer):
    porter =  RefPorterStemmer()

    def process_word(self,word):
        """ @return: porter stemming of the word
        """
        return self.porter.stem(word, 0, len(word)-1)
    
class LowerStemmer(BaseStemmer):
    def process_word(self,word):
        """ @return: porter stemming of the word
        """
        return word.lower()
    
    
class ComplexStemmer(BaseStemmer):   
    """ Agregates number of stemmers into chain """
    
    def __init__(self, *stemmers_list):
        '''        Constructor        '''                                 
        self.stemmers_list =  stemmers_list
            
    def process_word(self,word):
        """ @return: porter stemming of the word
        """
        for stemmer in self.stemmers_list:
            if word is None: return None
            word = stemmer.process_word(word)
        
        return word


_steammers_list = [ BaseStemmer(), StopWordsStemmer(), PorterStemmer() ]    
_steammers_map =  { stemmer.get_name():stemmer for stemmer in _steammers_list }

def get_stemmer_by_name(name):
    """ @param name: name of stemmer
        @return: instance correnponding stemmer or None if not found
    """
    stemmer =  _steammers_map.get(name)
    return stemmer

