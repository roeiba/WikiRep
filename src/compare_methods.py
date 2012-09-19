from numpy import dot
from numpy.linalg import norm
'''
Created on Sep 19, 2012

@author: roeib
'''
def cosine_metrics(self, v1, v2):        
    similarity  = float(dot(v1,v2) / (norm(v1) * norm(v2)))
    return similarity