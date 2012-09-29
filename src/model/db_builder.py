'''
Created on Sep 28, 2012

@author: inesmeya
'''
import numpy as np
from concept import Concept 
from math import log10
from database_wrapper import DatabaseWrapper


def _build_index_by_words(word_list):
    ''' converts list of word to dictionary {word => it's index} '''
    index_by_word = dict([(word,i) for i,word in enumerate(word_list)])
    return index_by_word

def _bulid_word_index(concepts_list):
    "returns list of unique words from all concepts"
    words_set = set()
    for concept in concepts_list:
        words = concept.get_all_words()
        words_set.update(words)
    return list(words_set)

def _build_df(index_by_word,concepts_list):
    ''' Calculates df as defined at page 6 of 2009_full
        df[i] is number of documents, that contains term i
        index i corresponds to index_by_word dictionary
        
        @param index_by_word: {word => index}
        @param concepts_list: list of Concept
        @return: vector (list) of df
    '''
    df_vec = [0]*len(index_by_word)
    for concept in concepts_list:
        words = concept.get_all_words()
        for word in words:
            i = index_by_word[word]
            df_vec[i]+=1
    return df_vec 


def _build_wieght_table(df_vec,index_by_word,concepts_list):
    ''' Creates not normalized Inverted Table as described on page 6 of 2009_full
    @param df_vec: df_vec[i] - number of documents, in witch word with index i appered 
    @param index_by_word: { word => index }
    @param concepts_list
    '''
    
    n = len(concepts_list)
    m = len(df_vec)
    T = np.zeros(shape=(m,n))
    for j, concept in enumerate(concepts_list):
        words = concept.get_all_words()
        for word in words:
            i =  index_by_word[word]
            tf_ij = concept.get_tf(word)
            
            T[i,j] = tf_ij * log10( n / df_vec[i] )
    return T



class DbBuilder(object):
    '''
    Current implementation doesn't check for concept duplications
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
        
        #uniqe enumeration of words
        word_index = _bulid_word_index(self.concepts_list)
        
        #word => index in word_index
        index_by_word = _build_index_by_words(word_index)
        
        # docs per word
        df_vec = _build_df(index_by_word, self.concepts_list)
        
        # wieght table not normilized
        T = _build_wieght_table(df_vec, index_by_word, self.concepts_list)
        
        #TODO: add normalization
        db = DatabaseWrapper(T, self.concepts_list, word_index)
        
        return db

        
        
        
                