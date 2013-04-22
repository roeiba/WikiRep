from scipy.linalg import norm
from scipy.sparse import csr_matrix as matrix
from math import log

from model.logger import getLogger
_log = getLogger(__name__)

#TODO: use scipy.spatial.distance for metrics  
def cosine_metrics(v1, v2):
    # for same vectors
    if v1 == v2: return 1.0
    
    # treat zero vectors
    denom = norm(v1.todense()) * norm(v2.todense()) 
    if denom == 0.0:
        _log.warning("One of the vectors is zero!")
        return 0.0
        _
    similarity  = v1.dot(v2.T) / denom
    return float(similarity[0,0])

def get_vectors_centroid(list_of_vectors):
    """ gets a list of scipy vectors with same dimensions and returns their centroid"""
    n = len(list_of_vectors)
    if n == 0: return
    #on 1d vector, shape holds the length
    shape = list_of_vectors[0].shape
    ret_vec = matrix(shape)
    for vector in list_of_vectors:
        _log.debug("get_vectors_centroid: Adding vector {}".format(vector))
        ret_vec = ret_vec + vector
    ret_vec = ret_vec * (1.0 / n) 
    return ret_vec 

def count_to_tf(count):
    if count == 0: 
        return 0
    else:          
        return 1 + log(count)
    
#TODO: normalization can be improved by using  (row.data**2).sum()
def normL2(T,row):
    i = row
    _,m = T.shape
    s = 0
    for l in xrange(m): 
        s += T[i,l]*T[i,l]
    the_norm = s**0.5
    return the_norm
    
def normalize(T):   
    n,m = T.shape
    for i in xrange(n):
        denom = normL2(T,i)
        if denom == 0.0: continue    
        for j in xrange(m): 
            T[i,j] = T[i,j]/ denom
    
