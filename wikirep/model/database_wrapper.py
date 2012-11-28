'''
Created on Sep 27, 2012

@author: roeib
'''
import scipy
from build_utils import build_index_by_words
from scipy.sparse import csr_matrix as matrix
from model.logger import *

class DatabaseWrapper(object):
    def __init__(self, wieght_matrix, concepts_index, words_index):
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
    
    def get_titles_index(self):
        return self.title_index
    
    def get_word_vector(self, word):
        """ Return:
                row representation of the word in Wiki concepts
        """
        vector = None
        if self.index_by_word.has_key(word):
            index = self.index_by_word[word]
            vector = self.wieght_matrix[index, :]
        else:
            #if word is not in corpus: return empty vector            
            vector = matrix((1,self.concepts_num))
        return vector
