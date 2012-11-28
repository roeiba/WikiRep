from scipy import dot
from scipy.linalg import norm
from scipy.sparse import csr_matrix as matrix
from scipy.sparse import issparse
from math import log
from model.logger import *
'''
Created on Sep 19, 2012

@author: roeib
'''
def cosine_metrics(v1, v2):        
    similarity  = v1.dot(v2.T) / (norm(v1.data) * norm(v2.data)) 
    return float(similarity[0,0])

def get_vectors_centroid(list_of_vectors):
    """ gets a list of scipy vectors with same dimensions and returns their centroid"""
    n = len(list_of_vectors)
    if n == 0: return
    #on 1d vector, shape holds the length
    shape = list_of_vectors[0].shape
    ret_vec = matrix(shape)
    for vector in list_of_vectors:
        DEBUG("get_vectors_centroid: Adding vector {}".format(vector))
        ret_vec = ret_vec + vector
    ret_vec = ret_vec * (1.0 / n) 
    return ret_vec 

def count_to_tf(count):
    if count == 0: 
        return 0
    else:          
        return 1 + log(count)
