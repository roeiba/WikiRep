import numpy

def load_db_from_file(filepath):
    pass

def load_db_stub():
    print "Running Test..." 
    doc1="I like to eat chicken\nnoodle soup."
    doc2="I have read the book \"Chicken noodle soup for the soul\"."
    print "Using Doc1: %s\n\nUsing Doc2: %s\n" % ( doc1, doc2 )
    return 

def get_vectors_centroid(list_of_vectors):
    """ gets a list of numpy vectors with same dimensions and returns their centroid"""
    n = len(list_of_vectors)
    if n == 0: return
    #on 1d vector, shape holds the length
    size = list_of_vectors[0].shape
    ret_vec = numpy.zeros(size)
    for vector in list_of_vectors:
        ret_vec += vector
    ret_vec *= (1.0 / n) 
    return ret_vec 