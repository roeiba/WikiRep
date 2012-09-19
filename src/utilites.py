
class VectorComparer(object):
    def compare_vectors(self, weighted_vector_1, weighted_vector_2):
        """ Gets two texts and returns the relatedness vector
        """
        raise NotImplemented("Abstract class")
    
class CosineMeasureComparer(VectorComparer):
    

def load_db_from_file(filepath):
    pass

def load_db_stub():
    print "Running Test..." 
    doc1="I like to eat chicken\nnoodle soup."
    doc2="I have read the book \"Chicken noodle soup for the soul\"."
    print "Using Doc1: %s\n\nUsing Doc2: %s\n" % ( doc1, doc2 )
    return 