import math_utils 
from database_wrapper import DatabaseWrapper

        
class SemanticInterpreter(object):
    def __init__(self, database, stemmer):
        assert type(database) == DatabaseWrapper, "DatabaseWrapper class is expected as database" 
        self.db = database
        self.stemmer = stemmer
        
    def get_weight_vector(self, word):
        """ Return:
                row representation of the word in Wiki concepts
        """
        index = self.db.words_index.index(word)
        return self.db.wieght_matrix[index, :]
    
    def build_weighted_vector(self, text):
        """ Gets a text and returns its weighted vector according the database """
        words_vectors = []
        words = self.stemmer.process_text(text)
        print words
        for word in words:
            word_wieght_vec = self.get_weight_vector(word)
            words_vectors.append(word_wieght_vec)
            print word_wieght_vec
        return math_utils.get_vectors_centroid(words_vectors)
        
