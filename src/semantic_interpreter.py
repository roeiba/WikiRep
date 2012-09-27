import utilities as utils
import numpy

class DatabaseWrapper(object):
    def __init__(self, wieght_matrix, concepts_index, words_index):
        #input validations
        assert type(wieght_matrix) != numpy.ndarray, "wieght_matrix is expected to be numpy.matrix"
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
    
        
class SemanticInterpreter(object):
    def __init(self, database, stemmer):
        assert type(database) == DatabaseWrapper, "DatabaseWrapper class is expected as database" 
        self.db = database
        self.stemmer = stemmer
        
    def get_weight_vector(self, word):
        """ Return:
                row representation of the word in Wiki concepts
        """
        index = self.words_index.index(word)
        return self.db.wieght_matrix[index, :]
    
    def build_weighted_vector(self, text):
        """ Gets a text and returns its weighted vector according the database """
        words_vectors = []
        for word in self.stemmer.process_text(text):
            word_wieght_vec = self.get_weight_vector(word)
            words_vectors.append(word_wieght_vec)
        return utils.get_vectors_centroid(words_vectors)
        
            
    
    
