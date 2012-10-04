from numpy import dot
from numpy.linalg import norm

import numpy as np
from math import log
'''
Created on Sep 19, 2012

@author: roeib
'''
def cosine_metrics(self, v1, v2):        
    similarity  = float(dot(v1,v2) / (norm(v1) * norm(v2)))
    return similarity

def get_vectors_centroid(list_of_vectors):
    """ gets a list of numpy vectors with same dimensions and returns their centroid"""
    n = len(list_of_vectors)
    if n == 0: return
    #on 1d vector, shape holds the length
    size = list_of_vectors[0].shape
    ret_vec = np.zeros(size)
    for vector in list_of_vectors:
        ret_vec += vector
    ret_vec *= (1.0 / n) 
    return ret_vec 

def count_to_tf(count):
    if count == 0: return 0
    else:          return 1 + log(count)
