import math_utils 
from database_wrapper import DatabaseWrapper
import logging

logger = logging.getLogger("Comparer")

class SemanticComparer(object):
    def __init__(self, db_wrapper, compare_method=None):
        """
        @param DatabaseWrapper database: Words inverted table
        @param compare_method: Method comparing vecors if None
        
        """
        assert type(db_wrapper) == DatabaseWrapper, "DatabaseWrapper class is expected as database" 
        self.db = db_wrapper
        
        self.compare_method = compare_method if compare_method else math_utils.cosine_metrics

    def compare(self, text1, text2):
        """
            Compares two texts in wikipedia space.
            @param db: WikiRep database filename
        """
        #semantic_interpreter = SemanticInterpreter(database)
        #generate weighted vectors
        msg_format = "Text: {text}\nWieght vector: {vector}"
        
        w_vector_1 = self.get_text_value(text1)
        logger.debug( msg_format.format(text=text1, vector=w_vector_1) )
        
        w_vector_2 = self.get_text_value(text2)
        logger.debug( msg_format.format(text=text2, vector=w_vector_2) )
        
        #compare vectors
        correlation = self.compare_method(w_vector_1, w_vector_2)
        logger.debug( "correlation is: {}".format(correlation) )
        return correlation
        
