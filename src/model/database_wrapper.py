'''
Created on Sep 27, 2012

@author: roeib
'''
import numpy

class DatabaseWrapper(object):
    def __init__(self, wieght_matrix, concepts_index, words_index):
        #input validations
        assert type(wieght_matrix) == numpy.ndarray, "wieght_matrix is expected to be numpy.matrix"
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
        self.title_index = map(lambda c: c.title,self.concepts_index)
    
    def get_titels_index(self):
        return self.title_index