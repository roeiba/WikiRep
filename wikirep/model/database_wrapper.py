'''
Created on Sep 27, 2012

@author: roeib
'''
import scipy
from scipy.sparse import csr_matrix as matrix
from build_utils import build_index_by_words
import math_utils
from model import stemmers 

from model.logger import *
import pickle

class DbContant(object):
    
    def __init__(self, weight_matrix, concepts_index, words_index,stemmer_name):
        """ Representd build data for using
        @param weight_matrix: matrix (concepts x words) 
            each row represents vector for specific word
        @param concepts_index: 
          concepts_index    
          
          """
        self.weight_matrix = weight_matrix
        self.concepts_index = concepts_index
        self.words_index = words_index 
        self.stemmer_name = stemmer_name



class DatabaseWrapper(object):
    def __init__(self, wieght_matrix, concepts_index, words_index, stemmer):
        #input validations
        #if type(wieght_matrix) == matrix:
        #    WARNING("wieght_matrix is expected to be scipy.sprase.csr_matrix, and not {}".format(type(wieght_matrix)))
            
        words_num = wieght_matrix.shape[0] #number of rows
        concepts_num = wieght_matrix.shape[1] #number of columns
        assert words_num == len(words_index), "Words index doesn't match matrix dimensions"
        assert concepts_num == len(concepts_index), "Concepts index doesn't match matrix dimensions"
        
        #assign variables
        self.concepts_index = concepts_index
        self.concepts_num = len(self.concepts_index)
        self.words_index = words_index
        self.words_num = len(self.words_index)
        self.wieght_matrix = wieght_matrix
        
        self.title_index = [c.title for c in concepts_index]
        self.index_by_word = build_index_by_words(words_index)
        
        self.stemmer = stemmer
    
    def get_titles_index(self):
        return self.title_index
    
    def get_word_vector(self, word):
        """ 
            Row representation of the word in Wiki concepts
            @returns: the text vector in wikipedia space.
        """
        vector = None
        if self.index_by_word.has_key(word):
            index = self.index_by_word[word]
            vector = self.wieght_matrix[index, :]
        else:
            #if word is not in corpus: return empty vector            
            vector = matrix((1,self.concepts_num))
        return vector
    
    def get_text_centroid(self, text):
        """ Gets a text and returns its weighted vector according the database """
        words_vectors = []
        words = self.stemmer.process_text(text)

        for word in words:
            if word in self.index_by_word: #filter terms, which not appear in the db
                word_wieght_vec = self.get_word_vector(word)
                words_vectors.append(word_wieght_vec)
            
        return math_utils.get_vectors_centroid(words_vectors)
    
    def get_readable_centroid(self,text):
        v = self.get_text_centroid(text).todense()[0]
        d = {self.title_index[i]: v[0,i] for i in xrange(self.concepts_num)}
        return d
    
    def get_word_dict(self,word):
        """ Returns dictionary with concept=>value """
        d = {}
        v = self.get_word_vector(word)
        for i,t in enumerate(self.title_index):
            d[t] = v[0,i]
        return d
    
    def to_dict_repr(self):
        """ Returns dictianry representation of db wrapper
            word => { Concept:value }
        """
        d = {w:self.get_word_dict(w) for w in self.words_index}
        return d