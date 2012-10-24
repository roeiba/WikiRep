'''
Created on Oct 4, 2012

@author: inesmeya
'''
import numpy as np
from math import log

def build_index_by_words(word_list):
    ''' converts list of word to dictionary {word => it's index} '''
    index_by_word = dict([(word,i) for i,word in enumerate(word_list)])
    return index_by_word


def build_word_index_back(concepts_list):
    """
    returns list of unique words from all concepts
    
    this method is identical to build_word_index
    #TODO: compare methods
    """
    words_set = set()
    for concept in concepts_list:
        words = concept.get_all_words()
        words_set.update(words)
    return list(words_set)

def build_word_index(concepts_list):
    """
    returns list of unique words from all concepts
    
    this method is identical to build_word_index_back
    #TODO: compare methods
    """
    words_set = set()
    words_list = []
    for concept in concepts_list:
        for word in concept.get_all_words():
            if  word not in words_set:
                words_list.append(word)
                words_set.add(word)
    return words_list

def build_df(index_by_word,concepts_list):
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


def build_wieght_table(df_vec,index_by_word,concepts_list):
    ''' Creates not normalized Inverted Table as described on page 6 of 2009_full
    @param df_vec: df_vec[i] - number of documents, in witch word with index i appered 
    @param index_by_word: { word => index }
    @param concepts_list
    '''
    
    n = float(len(concepts_list))
    m = len(df_vec)
    T = np.zeros(shape=(m,n))
    for j, concept in enumerate(concepts_list):
        words = concept.get_all_words()
        for word in words:
            i =  index_by_word[word]
            tf_ij = concept.get_tf(word)
            
            T[i,j] = tf_ij * log( n / df_vec[i] )
    return T 

