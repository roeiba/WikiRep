from semantic_interpreter import SemanticInterpreter
import utilites


filepath = ""
text_1 = ""
text_2 = ""


def main():
    #load database 
    database = utilites.load_db_from_file(filepath)
    
    #init interpreter
    semantic_interpreter = SemanticInterpreter(database)
 
    #generate weighted vectors
    w_vector_1 = semantic_interpreter.build_weighted_vector(text_1) 
    w_vector_2 = semantic_interpreter.build_weighted_vector(text_2)
    
    #compare vectors
    correlation = utilites.compare_vectors(w_vector_1, w_vector_2)
    print "correlation is: {}".format(correlation)
    
if __name__ == '__main__':
    main() 
    
    
class ConceptsDb(object):
    
    def get_concept_vector(self,word):
        """ Returns {} of word waight
            { concetp => concept weight,...}
        """
        
        pass
    

        
class ConceptsDbStub(ConceptsDb):
    
    def __init__(self):
        self.concepts = ["concept1","concept2"]
        self.db = {
            'word1' : [ 0.5, 0.0],
            'word2' : [ 0.3, 0.7]
        }
        
    def get_concept_vector(self,word):
        """returns word's weigted vector
        """
        return self.db[word]
    
    def get_concept_index(self,concept):
        """Returns index of specified concept
        """
        return self.concepts.index(concept)
        
        
       
       
       
        
        """ Returns {} of word waight
            { concetp => concept weight,...}
        """
        
        pass
    
    
    
    