from semantic_interpreter import SemanticInterpreter
import compare_methods
import utilities as utils

filepath = ""
text_1 = ""
text_2 = ""


def main():
    #load database 
    #database = utilites.load_db_from_file(filepath)
    database = utils.load_db_stub(filepath)
    
    #init interpreter
    semantic_interpreter = SemanticInterpreter(database)
 
    #generate weighted vectors
    w_vector_1 = semantic_interpreter.build_weighted_vector(text_1) 
    w_vector_2 = semantic_interpreter.build_weighted_vector(text_2)
    
    #compare vectors
    correlation = compare_methods.cosine_metrics(w_vector_1, w_vector_2)
    print "correlation is: {}".format(correlation)
    
if __name__ == '__main__':
    main() 
    
    
